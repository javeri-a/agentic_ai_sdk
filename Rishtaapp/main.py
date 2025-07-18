import streamlit as st
import os
import asyncio
import requests
from dotenv import load_dotenv

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# --------------------------
# Load .env
# --------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ULTRAMSG_INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")

ULTRAMSG_BASE_URL = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"


# --------------------------
# WhatsApp Function
# --------------------------
def send_whatsapp_message(phone_number, message):
    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": phone_number,
        "body": message
    }
    response = requests.post(ULTRAMSG_BASE_URL, json=payload)
    return response.json()


# --------------------------
# Rishtay Wali Auntie Agent
# --------------------------
async def run_rishtay_auntie(user_data):
    MODEL_NAME = "gemini-2.0-flash"

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

    auntie = Agent(
        name="Trusted Wedding Choice",
        instructions=(
            "Tum aik modern soch ki Rishtay Wali Auntie ho. "
            "User ki detail sun kar unke liye behtareen rishta dhoondh kr usy details do  clear details ke sath.    "
            "Respect sy or english me."
            "Tumhe sirf user ki details par amal karna hai, aur unki taraf se koi aur information nahi leni." \
                "Tumhe sirf WhatsApp par message bhejna hai, aur kisi aur platform par nahi."
                
        )
    )

    prompt = (
        f"Name: {user_data['name']}\n"
        f"Age: {user_data['age']}\n"
        f"Qualification: {user_data['qualification']}\n"
        f"Height: {user_data['height']} cm\n"
        f"Profession: {user_data['profession']}\n"
        f"Partner Preference: {user_data['partner_pref']}\n\n"
        "In sab ko dekh kar ek acha rishta dhoondho, details ke sath batao."
    )

    result = await Runner.run(
        starting_agent=auntie,
        input=prompt,
        run_config=config
    )

    return result.final_output


# --------------------------
# Streamlit App
# --------------------------
st.set_page_config(page_title="🤝 Trusted Wedding Choice", page_icon="💍", layout="centered")

# Custom CSS for beautiful look
st.markdown("""
    <style>
    body {
        background-color: #fdf6f0;
        color: #333333;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        color: #b08968;
        font-family: 'Georgia', serif;
    }
    .stButton button {
        background-color: #b08968;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-size: 1.1rem;
    }
    .stButton button:hover {
        background-color: #a67c52;
        color: #ffffff;
    }
    input, textarea {
        border-radius: 6px !important;
        border: 1px solid #d5c4a1 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💍 Trusted Wedding Choice 💍")
st.markdown(
    "<p style='text-align: center; font-size: 1.1rem; color: #5f4b32;'>"
    "WELCOME TO THE TRUSTED WEDDING CHOICE!<br>"
    "We Choose the Best Wedding Matches for You!<br>" \
    "This is a modern and respectful way to find your perfect match.<br>" \
    "Please fill out your details below to get started!<br>"
    "</p>",
    unsafe_allow_html=True
)

with st.form("rishta_form"):
    st.markdown("#### Please Enter your Details:")
    name = st.text_input("👤 Name:")
    whatsapp_number = st.text_input("📱 WhatsApp Number (with +countrycode)")
    age = st.number_input("🎂 Age", min_value=18, max_value=100)
    qualification = st.text_input("🎓 Education")
    height = st.number_input("📏 Height(inch)")
    profession = st.text_input("💼 Profession")
    partner_pref = st.text_area("❤️ What you want in a partner?")
    submitted = st.form_submit_button("Find Match 💍")

if submitted:
    user_data = {
        "name": name,
        "number": whatsapp_number,
        "age": age,
        "qualification": qualification,
        "height": height,
        "profession": profession,
        "partner_pref": partner_pref
    }

    with st.spinner("⏳ Trusted Wedding Choice is finding the best match..."):
        rishta_result = asyncio.run(run_rishtay_auntie(user_data))

    st.success("🎉 your best match is ready! Congratulations!")

    st.markdown("### 📜 Proposal Details:")
    st.write(rishta_result)

    with st.spinner("📲 Your match is sending you a message in Whatsapp..."):
        wa_response = send_whatsapp_message(user_data['number'],rishta_result)

    if wa_response.get("sent"):
        st.success("✅ WhatsApp bhej diya gaya hai! Aapka rishta aapko WhatsApp par mil jayega.")
    else:
        st.error(f"❌ WhatsApp bhejne mein masla: {wa_response}")