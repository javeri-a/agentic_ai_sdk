



from dotenv import load_dotenv
import os
import streamlit as st
import asyncio

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
from twilio.rest import Client

# Load environment variables
load_dotenv()

# Twilio config
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = 'whatsapp:+14155238886'  # Twilio Sandbox number

# Gemini config
MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup Gemini Client
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Send WhatsApp message
def send_whatsapp_message(to_number, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    msg = client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=f'whatsapp:{to_number}'
    )
    return msg.sid

# Run Gemini Agent
async def run_agent(prompt):
    assistant = Agent(
        name="AppointmentAssistant",
        instructions="You help confirm polite appointment reminders.",
    )
    result = await Runner.run(assistant, prompt, run_config=config)
    return result.final_output

# Streamlit UI
def main():
    st.title("📅 Appointment Reminder Bot (Gemini + WhatsApp)")

    with st.form("reminder_form"):
        name = st.text_input("Client Name", placeholder="Javeria")
        phone = st.text_input("WhatsApp Number (with country code)", placeholder="+923001234567")
        date = st.date_input("Appointment Date")
        time = st.time_input("Appointment Time")
        note = st.text_area("Appointment Note / Purpose", placeholder="Dental checkup")
        submit = st.form_submit_button("📤 Send Reminder")

    if submit:
        if not all([name, phone, date, time]):
            st.warning("Please fill all fields.")
            return

        prompt = (
            f"Write a friendly WhatsApp reminder for {name} "
            f"about their appointment for '{note}' on {date} at {time}."
        )

        # Run agent & send message
        with st.spinner("⏳ Generating reminder..."):
            final_message = asyncio.run(run_agent(prompt))
            st.write("🤖 **AI Reminder:**", final_message)

        with st.spinner("📲 Sending WhatsApp message..."):
            try:
                sid = send_whatsapp_message(phone, final_message)
                st.success(f"✅ WhatsApp sent! SID: {sid}")
            except Exception as e:
                st.error(f"❌ Error sending message: {e}")

if __name__ == "__main__":
    main()
