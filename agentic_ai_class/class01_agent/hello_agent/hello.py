
import streamlit as st
from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio
import datetime


load_dotenv()


st.set_page_config(
    page_title="Javi Connect Dev",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="🤖"
)


st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(to right, #f8fbff, #eef4f7);
    font-family: 'Segoe UI', sans-serif;
}

/* Chat container */
.chat-container {
    max-width: 850px;
    margin: 2rem auto;
    background: #ffffffee;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}

/* Title */
h1 {
    font-weight: 800;
    color: #1f2c33;
    text-align: center;
}

/* Input and button styling */
input[type="text"] {
    border: 2px solid #3498db;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    width: 100%;
    font-size: 1rem;
}

.stButton > button {
    background-color: #2ecc71;
    color: white;
    font-weight: bold;
    padding: 0.6rem 2rem;
    border-radius: 10px;
    border: none;
    margin-top: 0.8rem;
}

.stButton > button:hover {
    background-color: #27ae60;
    transform: scale(1.03);
}

/* Chat bubble */
.chat-msg {
    padding: 1rem 1.4rem;
    border-radius: 15px;
    margin-bottom: 1.2rem;
    line-height: 1.6;
    font-size: 1rem;
    width: fit-content;
    max-width: 75%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.user-msg {
    background-color: #3498db;
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 0;
}

.bot-msg {
    background-color: #ecf0f1;
    color: #2c3e50;
    margin-right: auto;
    border-bottom-left-radius: 0;
}

.meta {
    font-size: 0.75rem;
    color: #7f8c8d;
    margin-top: 0.2rem;
    text-align: right;
}

/* Scroll container */
.chat-history {
    max-height: 500px;
    overflow-y: auto;
    padding-right: 1rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("🤖 Javi Connect Dev")
st.markdown("Welcome to your AI-powered assistant! Ask anything below.")


if 'history' not in st.session_state:
    st.session_state.history = []

def append_to_history(role, message):
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    st.session_state.history.append({"role": role, "message": message, "time": timestamp})


with st.form(key='chat_form', clear_on_submit=True):
    query = st.text_input("Ask Javi:", placeholder="What would you like help with?")
    submit = st.form_submit_button("Send")

if submit and query.strip():
    append_to_history("user", query)

    with st.spinner("Javi is thinking..."):
        async def run_response():
            GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
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

            assistant = Agent(
                name="Javi",
                instructions="You are a helpful assistant developed for Javi Connect Dev. Answer thoughtfully and clearly.",
            )

            result = await Runner.run(assistant, query, run_config=config)
            return result.final_output

        answer = asyncio.run(run_response())
        append_to_history("bot", answer)

st.markdown('<div class="chat-history">', unsafe_allow_html=True)

for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f'''
        <div class="chat-msg user-msg">{chat["message"]}<div class="meta">You • {chat["time"]}</div></div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="chat-msg bot-msg">{chat["message"]}<div class="meta">Javi • {chat["time"]}</div></div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
