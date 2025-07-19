

# import streamlit as st
# import asyncio
# import os
# from dotenv import load_dotenv
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
# from concurrent.futures import ThreadPoolExecutor

# # Load .env file
# load_dotenv()

# # Model details
# MODEL_NAME = "gemini-2.0-flash"
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # Create external client & model
# external_client = AsyncOpenAI(
#     api_key=GEMINI_API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model=MODEL_NAME,
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # ---------- ASYNC AGENT FUNCTION ----------
# async def my_agent_function_async(user_message: str):
#     assistant = Agent(
#         name="Javeria Assistant",
#         instructions=(
#             "You are Javeria — a front-end developer and agentic AI builder. "
#             "You help people by answering their questions warmly and clearly, "
#             "explaining how your services can help them succeed."
#         )
#     )
#     result = await Runner.run(assistant, user_message, run_config=config)
#     return result.final_output

# # ---------- SAFE SYNC WRAPPER ----------
# def my_agent_function(user_message: str):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     return loop.run_until_complete(my_agent_function_async(user_message))


# # ---------- STREAMLIT UI ----------
# st.set_page_config(page_title="Welcome to Javeria", page_icon="👋")

# st.title("👋 Welcome to Javeria")

# # Initialize chat state
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": (
#                 "Hey! I’m Javeria — a front-end developer and agentic AI builder. "
#                 "I help people and businesses turn their ideas into smart, user-friendly digital products. "
#                 "Whether you need a modern web interface, a custom AI agent, or an SDK that just works, "
#                 "I’m here to make it happen smoothly.\n\n"
#                 "My focus is clear code, clean design, and reliable solutions that save you time "
#                 "and make your work easier. From smart automations to beautiful front-end experiences, "
#                 "I build what fits your goals — not just what looks good on paper.\n\n"
#                 "Explore my work here:\n"
#                 "- [🌐 Portfolio](https://yourportfolio.com)\n"
#                 "- [💼 LinkedIn](https://linkedin.com/in/yourprofile)\n"
#                 "- [🐙 GitHub](https://github.com/yourusername)\n"
#                 "- [📧 Email](mailto:javiconnectdev@gmail.com)\n\n"
#                 "So, how can I help you today?"
#             )
#         }
#     ]

# # Show chat history
# for msg in st.session_state.messages:
#     if msg["role"] == "assistant":
#         st.markdown(f"**Javeria:** {msg['content']}")
#     else:
#         st.markdown(f"**You:** {msg['content']}")

# # User input
# prompt = st.text_input("Your message:", key="user_input")

# if st.button("Send"):
#     if prompt.strip() != "":
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         # Run agent in separate thread
#         with ThreadPoolExecutor() as executor:
#             response = executor.submit(my_agent_function, prompt).result()

#         st.session_state.messages.append({"role": "assistant", "content": response})

#         # SAFE rerun for your Streamlit version
#         st.rerun()






import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
from concurrent.futures import ThreadPoolExecutor

# ---------------- ENV ----------------
load_dotenv()

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

# ---------------- AGENT FUNCTION ----------------
async def my_agent_function_async(user_message: str):
    assistant = Agent(
        name="Javeria Assistant",
        instructions=(
            "You are Javeria — a front-end developer and agentic AI builder. "
            "Answer clearly and warmly, focus on showing how your services help."
        )
    )
    result = await Runner.run(assistant, user_message, run_config=config)
    return result.final_output

def my_agent_function(user_message: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(my_agent_function_async(user_message))

# ---------------- STREAMLIT ----------------
st.set_page_config(page_title="Welcome to Javeria", page_icon="👋")
st.title("👋 Welcome to Javeria")

# ---------- Chat state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
    # First welcome only once
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Hey! I’m Javeria — a front-end developer and agentic AI builder. "
            "I help you turn ideas into smart, user-friendly digital products. "
            "From modern web UIs to custom AI agents and SDKs — I deliver clear code, clean design, "
            "and reliable solutions.\n\n"
            "Check my work:\n"
            "- [🌐 Portfolio](https://yourportfolio.com)\n"
            "- [💼 LinkedIn](https://linkedin.com/in/yourprofile)\n"
            "- [🐙 GitHub](https://github.com/yourusername)\n"
            "- [📧 Email](mailto:javiconnectdev@gmail.com)\n\n"
            "How can I help you today?"
        )
    })

# ---------- Display chat ----------
for msg in st.session_state.messages:
    speaker = "Javeria" if msg["role"] == "assistant" else "You"
    st.markdown(f"**{speaker}:** {msg['content']}")

# ---------- User input ----------
prompt = st.text_input("Type your message:", key="user_input")

if st.button("Send"):
    if prompt.strip():
        st.session_state.messages.append({"role": "user", "content": prompt})

        with ThreadPoolExecutor() as executor:
            response = executor.submit(my_agent_function, prompt).result()

        st.session_state.messages.append({"role": "assistant", "content": response})

        st.rerun()
