import streamlit as st
from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio
import datetime

load_dotenv()

st.set_page_config(
    page_title="Javbot",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="🤖"
)

# خوبصورت اور رنگین CSS اسٹائل
st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #f0f0f0;
}

/* Chat container */
.chat-container {
    max-width: 900px;
    margin: 3rem auto;
    background: linear-gradient(145deg, #1f2937, #111827);
    padding: 3rem 3.5rem;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7);
    border: 1px solid #3b82f6;
}

/* Title */
h1 {
    font-weight: 900;
    color: #3b82f6;
    text-align: center;
    font-size: 3rem;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 8px #3b82f6;
}

/* Subtitle */
h2, .stMarkdown p {
    color: #9ca3af;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: 400;
    font-size: 1.15rem;
}

/* Input and button styling */
input[type="text"] {
    border: none;
    border-radius: 15px;
    padding: 1rem 1.2rem;
    width: 100%;
    font-size: 1.2rem;
    outline: none;
    box-shadow: 0 0 12px #3b82f6aa;
    background: #111827;
    color: #e5e7eb;
    transition: box-shadow 0.3s ease;
}

input[type="text"]:focus {
    box-shadow: 0 0 20px #60a5fa;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
    color: white;
    font-weight: 700;
    padding: 0.8rem 2.5rem;
    border-radius: 20px;
    border: none;
    margin-top: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 1.1rem;
    box-shadow: 0 5px 15px #3b82f6cc;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2563eb, #2563ebcc);
    transform: scale(1.05);
    box-shadow: 0 8px 25px #2563ebcc;
}

/* Chat bubble */
.chat-msg {
    padding: 1rem 1.8rem;
    border-radius: 25px;
    margin-bottom: 1.3rem;
    line-height: 1.7;
    font-size: 1.1rem;
    max-width: 75%;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    position: relative;
    word-wrap: break-word;
    animation: fadeIn 0.3s ease forwards;
}

.user-msg {
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 5px;
}

.bot-msg {
    background: linear-gradient(135deg, #374151, #1f2937);
    color: #9ca3af;
    margin-right: auto;
    border-bottom-left-radius: 5px;
}

/* Meta info */
.meta {
    font-size: 0.7rem;
    color: #9ca3af;
    margin-top: 0.3rem;
    text-align: right;
}

/* Scroll container */
.chat-history {
    max-height: 520px;
    overflow-y: auto;
    padding-right: 1.2rem;
    scrollbar-width: thin;
    scrollbar-color: #2563eb #1f2937;
}

/* Scrollbar for Webkit browsers */
.chat-history::-webkit-scrollbar {
    width: 8px;
}

.chat-history::-webkit-scrollbar-track {
    background: #1f2937;
    border-radius: 10px;
}

.chat-history::-webkit-scrollbar-thumb {
    background: #2563eb;
    border-radius: 10px;
}

/* Fade in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# HTML container start
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.title("🤖 Welcome to JAVBOT")
st.markdown("Welcome to your AI-powered assistant! Ask anything below.")

if 'history' not in st.session_state:
    st.session_state.history = []

def append_to_history(role, message):
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    st.session_state.history.append({"role": role, "message": message, "time": timestamp})

with st.form(key='chat_form', clear_on_submit=True):
    query = st.text_input("Ask JavBOT:", placeholder="What would you like help with?")
    submit = st.form_submit_button("Send")

if submit and query.strip():
    append_to_history("user", query)

    with st.spinner("JavBOT is thinking..."):
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
st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container div