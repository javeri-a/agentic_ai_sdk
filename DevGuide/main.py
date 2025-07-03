
import streamlit as st
from dotenv import load_dotenv
import os
import asyncio

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

load_dotenv()

@st.cache_resource
def setup():
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

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

    assistant = Agent(
        name="DevGuider",
        instructions=(
            "You are DevCompass, a warm, encouraging, and clear guide for aspiring developers. "
            "You only answer questions related to developer careers, programming, software engineering, "
            "coding skills, and roadmaps. If asked anything unrelated, politely decline and guide the user "
            "back to developer topics."
        )
    )

    return assistant, config

assistant, config = setup()

st.set_page_config(
    page_title="DevGuider - Developer Guide",
    page_icon="💻",
    layout="wide"
)

with st.sidebar:
    st.title("DevGuider")
    st.write("**Your traditional yet modern guide to the world of coding!**")
    st.markdown("---")

    st.write("💡 **Try these:**")
    if st.button("📌 How do I become a frontend dev?"):
        st.session_state.messages.append({"role": "user", "content": "How do I become a frontend developer?"})

    if st.button("📌 Which language should I start with?"):
        st.session_state.messages.append({"role": "user", "content": "Which programming language should I start with?"})

    if st.button("📌 What is backend development?"):
        st.session_state.messages.append({"role": "user", "content": "What is backend development and what should I learn?"})

    st.markdown("---")
    st.write("📚 **Helpful Resources:**")
    st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
    st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
    st.markdown("- [W3Schools](https://www.w3schools.com/)")
    st.markdown("- [GitHub Explore](https://github.com/explore)")

    st.markdown("---")
    st.write("✨ *Built with ❤️ by Javeria*")

st.title("💬 Developer Guider Chatbot")
st.subheader("Welcome! Let DevGuider guide you through your programming journey.")
st.success("💡 *Quote of the day:* *“First, solve the problem. Then, write the code.” — John Johnson*")

# --- Helper: Check if input is dev-related ---
def is_dev_related(user_input):
    dev_keywords = [
        "developer", "development", "programming", "programmer",
        "coding", "code", "python", "javascript", "frontend",
        "backend", "fullstack", "software", "engineer", "career",
        "web development", "app development", "AI", "ML", "roadmap"
    ]
    user_input_lower = user_input.lower()
    return any(word in user_input_lower for word in dev_keywords)

# --- Helper: Check if greeting ---
def is_greeting(user_input):
    greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
    user_input_lower = user_input.lower()
    return any(word in user_input_lower for word in greetings)

# --- Chat Area ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your question about developer careers here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display placeholder for "thinking..."
    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("🤔 *Thinking...*")

    async def run_agent():
        # Handle greeting specially
        if is_greeting(prompt):
            return (
                "👋 Hello! I’m DevGuider, your guide to the world of coding and developer careers. "
                "How may I assist you today?"
            )

        # Handle non-dev related input
        if not is_dev_related(prompt):
            return (
                "🙏 I’m sorry, but I’m only designed to guide you about developer careers, coding, and programming. "
                "Please ask me something related to software development!"
            )

        result = await Runner.run(
            assistant,
            prompt,
            run_config=config
        )
        return result.final_output

    response = asyncio.run(run_agent())

    # Replace the placeholder with the final answer
    thinking_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# --- FAQ Section ---
with st.expander("📖 Frequently Asked Questions"):
    st.write("**Q1:** *Is coding hard?*")
    st.write("💬 Learning to code can be challenging at first, but with practice and guidance, anyone can master it.")
    st.write("**Q2:** *How long does it take to become a developer?*")
    st.write("💬 It depends on your pace and focus, but 6 months to 1 year is a common range for beginners.")
    st.write("**Q3:** *Do I need a CS degree?*")
    st.write("💬 No! Many developers are self-taught or have bootcamp certificates.")
    st.write("**Q4:** *What if I get stuck?*")
    st.write("💬 Always ask questions, join communities, and keep practicing.")
