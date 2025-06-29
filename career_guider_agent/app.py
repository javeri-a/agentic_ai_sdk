
import streamlit as st
from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio
import datetime

load_dotenv()

st.set_page_config(
    page_title="📚 Study Assistant JavBOT",
    layout="centered",
    page_icon="📚"
)

# Premium CSS
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
}

.chat-container {
    max-width: 750px;
    margin: 2rem auto;
    background: #ffffff;
    border-radius: 20px;
    padding: 2rem 2.5rem;
    box-shadow: 0 6px 30px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    color: #3b82f6;
    font-weight: 800;
    margin-bottom: 1rem;
}

.chat-history {
    display: flex;
    flex-direction: column;
}

.user-msg, .bot-msg {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    max-width: 90%;
}

.user-msg {
    flex-direction: row-reverse;
    margin-left: auto;
}

.bot-msg {
    flex-direction: row;
    margin-right: auto;
}

.bubble {
    padding: 0.85rem 1.2rem;
    border-radius: 18px;
    line-height: 1.6;
    font-size: 1rem;
    word-wrap: break-word;
}

.user-bubble {
    background: #3b82f6;
    color: white;
}

.bot-bubble {
    background: #f1f5f9;
    color: #111827;
}

.avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #3b82f6;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
}

.meta {
    font-size: 0.7rem;
    color: #666;
    margin-top: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.title("📚 Study Assistant JavBOT")

if 'history' not in st.session_state:
    st.session_state.history = []

def append_to_history(role, message):
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    st.session_state.history.append({"role": role, "message": message, "time": timestamp})

with st.form(key='chat_form', clear_on_submit=True):
    query = st.text_input("Ask your study question:", placeholder="Type your study question...")
    submit = st.form_submit_button("Send")

if submit and query.strip():
    append_to_history("user", query)

    with st.spinner("JavBOT is typing..."):
        async def run_response():
            GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
            MODEL_NAME = "gemini-2.0-flash"

            off_topic_keywords = [
                "weather", "news", "joke", "sports", "politics",
                "game", "music", "movie", "film", "travel", "food",
                "recipe", "fashion", "songs", "song", "technology"
            ]

            if any(word in query.lower() for word in off_topic_keywords):
                return "📚 *Main sirf Study Assistant hoon. Aap education ya study related poochain.*"

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
                name="JavBOT",
                instructions="""
You are a polite Study Assistant. You ONLY help with study-related questions.
If the user asks anything not related to study, politely say:
"Main sirf Study Assistant hoon. Aap education ya study related poochain."
Always answer in simple Urdu-English.
"""
            )

            result = await Runner.run(assistant, query, run_config=config)
            return result.final_output

        answer = asyncio.run(run_response())
        append_to_history("bot", answer)

# Display chat history with avatars and bubbles
st.markdown('<div class="chat-history">', unsafe_allow_html=True)

for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f'''
        <div class="user-msg">
            <div class="avatar">U</div>
            <div>
                <div class="bubble user-bubble">{chat["message"]}</div>
                <div class="meta">{chat["time"]}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="bot-msg">
            <div class="avatar">J</div>
            <div>
                <div class="bubble bot-bubble">{chat["message"]}</div>
                <div class="meta">{chat["time"]}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
