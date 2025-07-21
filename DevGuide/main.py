
import streamlit as st
from dotenv import load_dotenv
import os
import asyncio

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# --- Load environment variables ---
load_dotenv()

# --- Setup Agent ---
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
            "You are DevGuider, a warm, encouraging, and clear guide for aspiring developers. "
            "You ONLY answer questions related to developer careers, programming, software engineering, "
            "coding skills, and roadmaps. "
            "If asked anything unrelated, politely decline and guide the user back to developer topics. "
            "If the user provides code, always explain accurately what the code does. "
            "If the question is asked in any language, ALWAYS reply in English."
            
        )
    )

    return assistant, config

assistant, config = setup()

# --- Page Config ---
st.set_page_config(
    page_title="DevGuider",
    page_icon="💻",
    layout="wide"
)

# --- Theme CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 12px 18px;
        margin: 10px 0;
        line-height: 1.7;
        font-family: 'Segoe UI', sans-serif;
    }
    .stChatMessage.user {
        background: #d0ebff;
        text-align: right;
    }
    .stChatMessage.assistant {
        background: #ffffff;
        border-left: 4px solid #6a11cb;
        text-align: left;
    }
    .block-container {
        max-width: 800px;
        margin: auto;
    }

    /* Sidebar colors */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: #ffffff;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] a {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] a:hover {
        text-decoration: underline;
        color: #ffdd57 !important;
    }
    .sidebar-link {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("💜 DevGuider")
    st.markdown("*Your steady coding companion.*")
    st.write("---")

    # 🌟 Daily Coding Tip
    st.subheader("💡 Daily Coding Tip")
    st.info("Break big problems into small ones. One step at a time wins the race!")

    st.write("---")

 
    
    st.caption("✨ Crafted with devotion by Javeria")

# --- Greeting ---
st.title("💬 Developer Guider")
st.subheader("*Your professional, warm coding mentor.*")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Hello! I am DevGuider your personal guide for coding, developer careers, and practical help. Ask me anything!"
    })

# --- Keyword Checks ---
def is_dev_related(user_input):
    dev_keywords = [
        "developer", "development", "programming", "programmer",
        "coding", "code", "python", "javascript", "frontend",
        "backend", "fullstack", "software", "engineer", "career",
        "web development", "app development", "AI", "ML", "roadmap", "HTML", "CSS",
        "SQL", "database", "API", "framework", "library", "git",
        "version control", "agile", "scrum", "devops", "cloud",
        "docker", "kubernetes", "CI/CD", "testing", "debugging",
        "algorithm", "data structure", "architecture", "design pattern",
        "architecture", "best practices", "performance", "optimization",
        "security", "scalability", "accessibility", "usability", "UX", "UI",
        "mobile development", "web app", "software engineering", "tech stack",
    ]
    return any(word in user_input.lower() for word in dev_keywords)

def is_greeting(user_input):
    greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
    return any(word in user_input.lower() for word in greetings)

# --- Display Messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Input Box ---
if prompt := st.chat_input("Ask your coding question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown(" *Thinking...*")

        async def run_agent():
            if is_greeting(prompt):
                return (
                    "👋 Hello again! I am always ready to assist you with your coding journey."
                )
            if not is_dev_related(prompt):
                return (
                    "🙏 I apologise I answer only coding, programming and developer questions. Please ask something relevant."
                )
            result = await Runner.run(assistant, prompt, run_config=config)
            return result.final_output

        response = asyncio.run(run_agent())
        thinking_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
