# import streamlit as st
# from dotenv import load_dotenv
# import os
# import asyncio

# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# load_dotenv()

# @st.cache_resource
# def setup():
#     MODEL_NAME = "gemini-2.0-flash"
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#     external_client = AsyncOpenAI(
#         api_key=GEMINI_API_KEY,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )

#     model = OpenAIChatCompletionsModel(
#         model=MODEL_NAME,
#         openai_client=external_client
#     )

#     config = RunConfig(
#         model=model,
#         model_provider=external_client,
#         tracing_disabled=True
#     )

#     assistant = Agent(
#         name="DevGuider",
#         instructions=(
#             "You are DevCompass, a warm, encouraging, and clear guide for aspiring developers. "
#             "You only answer questions related to developer careers, programming, software engineering, "
#             "coding skills, and roadmaps. If asked anything unrelated, politely decline and guide the user "
#             "back to developer topics."
#         )
#     )

#     return assistant, config

# assistant, config = setup()

# st.set_page_config(
#     page_title="DevGuider - Developer Guide",
#     page_icon="💻",
#     layout="wide"
# )

# with st.sidebar:
#     st.title("DevGuider")
#     st.write("**Your traditional yet modern guide to the world of coding!**")
#     st.markdown("---")

#     st.write("💡 **Try these:**")
#     if st.button("📌 How do I become a frontend dev?"):
#         st.session_state.messages.append({"role": "user", "content": "How do I become a frontend developer?"})

#     if st.button("📌 Which language should I start with?"):
#         st.session_state.messages.append({"role": "user", "content": "Which programming language should I start with?"})

#     if st.button("📌 What is backend development?"):
#         st.session_state.messages.append({"role": "user", "content": "What is backend development and what should I learn?"})

#     st.markdown("---")
#     st.write("📚 **Helpful Resources:**")
#     st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
#     st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
#     st.markdown("- [W3Schools](https://www.w3schools.com/)")
#     st.markdown("- [GitHub Explore](https://github.com/explore)")

#     st.markdown("---")
#     st.write("✨ *Built with ❤️ by Javeria*")

# st.title("💬 Developer Guider Chatbot")
# st.subheader("Welcome! Let DevGuider guide you through your programming journey.")
# st.success("💡 *Quote of the day:* *“First, solve the problem. Then, write the code.” — John Johnson*")

# # --- Helper: Check if input is dev-related ---
# def is_dev_related(user_input):
#     dev_keywords = [
#         "developer", "development", "programming", "programmer",
#         "coding", "code", "python", "javascript", "frontend",
#         "backend", "fullstack", "software", "engineer", "career",
#         "web development", "app development", "AI", "ML", "roadmap"
#     ]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in dev_keywords)

# # --- Helper: Check if greeting ---
# def is_greeting(user_input):
#     greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in greetings)

# # --- Chat Area ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# if prompt := st.chat_input("Type your question about developer careers here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Display placeholder for "thinking..."
#     with st.chat_message("assistant"):
#         thinking_placeholder = st.empty()
#         thinking_placeholder.markdown("🤔 *Thinking...*")

#     async def run_agent():
#         # Handle greeting specially
#         if is_greeting(prompt):
#             return (
#                 "👋 Hello! I’m DevGuider, your guide to the world of coding and developer careers. "
#                 "How may I assist you today?"
#             )

        
#         if not is_dev_related(prompt):
#             return (
#                 "🙏 Iam sorry, but I’m only designed to guide you about developer careers, coding, and programming. "
#                 "Please ask me something related to software development!"
#             )

#         result = await Runner.run(
#             assistant,
#             prompt,
#             run_config=config
#         )
#         return result.final_output

#     response = asyncio.run(run_agent())

    
#     thinking_placeholder.markdown(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})

# # --- FAQ Section ---
# with st.expander("📖 Frequently Asked Questions"):
#     st.write("**Q1:** *Is coding hard?*")
#     st.write("💬 Learning to code can be challenging at first, but with practice and guidance, anyone can master it.")
#     st.write("**Q2:** *How long does it take to become a developer?*")
#     st.write("💬 It depends on your pace and focus, but 6 months to 1 year is a common range for beginners.")
#     st.write("**Q3:** *Do I need a CS degree?*")
#     st.write("💬 No! Many developers are self-taught or have bootcamp certificates.")
#     st.write("**Q4:** *What if I get stuck?*")
#     st.write("💬 Always ask questions, join communities, and keep practicing.")



# import streamlit as st
# from dotenv import load_dotenv
# import os
# import asyncio

# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# load_dotenv()

# @st.cache_resource
# def setup():
#     MODEL_NAME = "gemini-2.0-flash"
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#     external_client = AsyncOpenAI(
#         api_key=GEMINI_API_KEY,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )

#     model = OpenAIChatCompletionsModel(
#         model=MODEL_NAME,
#         openai_client=external_client
#     )

#     config = RunConfig(
#         model=model,
#         model_provider=external_client,
#         tracing_disabled=True
#     )

#     assistant = Agent(
#         name="DevGuider",
#         instructions=(
#             "You are DevGuider, a warm, encouraging, and clear guide for aspiring developers. "
#             "You ONLY answer questions related to developer careers, programming, software engineering, "
#             "coding skills, and roadmaps. "
#             "If asked anything unrelated, politely decline and guide the user back to developer topics. "
#             "If the user provides code, always explain accurately what the code does. "
#             "If the question is asked in any language, ALWAYS reply in English."
#         )
#     )

#     return assistant, config

# assistant, config = setup()

# st.set_page_config(
#     page_title="DevGuider - Developer Guide",
#     page_icon="💻",
#     layout="wide"
# )

# # --- Sidebar ---
# with st.sidebar:
#     st.title("DevGuider")
#     st.write("**Your traditional yet modern guide to the world of coding!**")
#     st.markdown("---")

#     st.write("💡 **Try these:**")
#     if st.button("📌 How do I become a frontend dev?"):
#         st.session_state.messages.append({"role": "user", "content": "How do I become a frontend developer?"})

#     if st.button("📌 Which language should I start with?"):
#         st.session_state.messages.append({"role": "user", "content": "Which programming language should I start with?"})

#     if st.button("📌 What is backend development?"):
#         st.session_state.messages.append({"role": "user", "content": "What is backend development and what should I learn?"})

#     st.markdown("---")
#     st.write("📚 **Helpful Resources:**")
#     st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
#     st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
#     st.markdown("- [W3Schools](https://www.w3schools.com/)")
#     st.markdown("- [GitHub Explore](https://github.com/explore)")

#     st.markdown("---")
#     st.write("✨ *Built with ❤️ by Javeria*")

# st.title("💬 Developer Guider Chatbot")
# st.subheader("Welcome! Let DevGuider guide you through your programming journey.")
# st.success("💡 *Quote of the day:* *“First, solve the problem. Then, write the code.” — John Johnson*")

# # --- Initialize chat history ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     # Add automatic greeting message when app loads
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "👋 Hello! I’m DevGuider — your clear and encouraging coding guide. "
#                    "Feel free to ask anything about web development, coding careers, or code explanations!"
#     })

# # --- Developer keywords ---
# def is_dev_related(user_input):
#     dev_keywords = [
#         "developer", "development", "programming", "programmer",
#         "coding", "code", "python", "javascript", "frontend",
#         "backend", "fullstack", "software", "engineer", "career",
#         "web development", "app development", "AI", "ML", "roadmap", "ai", "artificial intelligence", "machine learning" , "data science", "data analysis", "agentic ai sdk"
#     ]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in dev_keywords)

# # --- Greeting check ---
# def is_greeting(user_input):
#     greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in greetings)

# # --- Chat display ---
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # --- Chat input ---
# if prompt := st.chat_input("Type your question about developer careers or code here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Thinking placeholder
#     with st.chat_message("assistant"):
#         thinking_placeholder = st.empty()
#         thinking_placeholder.markdown("🤔 *Thinking...*")

#     async def run_agent():
#         # Handle greeting
#         if is_greeting(prompt):
#             return (
#                 "👋 Hello! I’m DevGuider, your guide to the world of coding and developer careers. "
#                 "How may I assist you today?"
#             )

#         # Non-dev related check
#         if not is_dev_related(prompt):
#             return (
#                 "🙏 I am sorry, but I’m only designed to guide you about developer careers, coding, "
#                 "and programming. Please ask me something related to software development!"
#             )

#         # If code block is present or question is about code, always explain
#         if "```" in prompt or "code" in prompt.lower():
#             instructions = (
#                 "Please clearly explain what the given code does, line by line if possible. "
#                 "Keep the answer simple and clear for a beginner. "
#                 "Always answer in English."
#             )
#             result = await Runner.run(
#                 assistant,
#                 prompt + "\n" + instructions,
#                 run_config=config
#             )
#             return result.final_output

#         # For normal developer questions
#         result = await Runner.run(
#             assistant,
#             prompt,
#             run_config=config
#         )
#         return result.final_output

#     response = asyncio.run(run_agent())

#     thinking_placeholder.markdown(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})

# # --- FAQ ---
# with st.expander("📖 Frequently Asked Questions"):
#     st.write("**Q1:** *Is coding hard?*")
#     st.write("💬 Learning to code can be challenging at first, but with practice and guidance, anyone can master it.")
#     st.write("**Q2:** *How long does it take to become a developer?*")
#     st.write("💬 It depends on your pace and focus, but 6 months to 1 year is a common range for beginners.")
#     st.write("**Q3:** *Do I need a CS degree?*")
#     st.write("💬 No! Many developers are self-taught or have bootcamp certificates.")
#     st.write("**Q4:** *What if I get stuck?*")
#     st.write("💬 Always ask questions, join communities, and keep practicing.")










































# import streamlit as st
# from dotenv import load_dotenv
# import os
# import asyncio

# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# load_dotenv()

# @st.cache_resource
# def setup():
#     MODEL_NAME = "gemini-2.0-flash"
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#     external_client = AsyncOpenAI(
#         api_key=GEMINI_API_KEY,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )

#     model = OpenAIChatCompletionsModel(
#         model=MODEL_NAME,
#         openai_client=external_client
#     )

#     config = RunConfig(
#         model=model,
#         model_provider=external_client,
#         tracing_disabled=True
#     )

#     assistant = Agent(
#         name="DevGuider",
#         instructions=(
#             "You are DevGuider, a warm, encouraging, and clear guide for aspiring developers. "
#             "You ONLY answer questions related to developer careers, programming, software engineering, "
#             "coding skills, and roadmaps. "
#             "If asked anything unrelated, politely decline and guide the user back to developer topics. "
#             "If the user provides code, always explain accurately what the code does. "
#             "If the question is asked in any language, ALWAYS reply in English."
#         )
#     )

#     return assistant, config

# assistant, config = setup()

# # --- Custom CSS ---
# st.markdown("""
#     <style>
#     body {
#         background-color: #f9f9f9;
#     }
#     .main {
#         background-color: #ffffff;
#         border-radius: 10px;
#         padding: 2rem;
#     }
#     .stButton button {
#         background-color: #4CAF50;
#         color: white;
#         border: none;
#         border-radius: 5px;
#     }
#     .stButton button:hover {
#         background-color: #45a049;
#     }
#     .stChatMessage {
#         border-radius: 10px;
#         padding: 10px;
#         margin-bottom: 10px;
#     }
#     .stChatMessage.user {
#         background-color: #e0f7fa;
#     }
#     .stChatMessage.assistant {
#         background-color: #f1f8e9;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- Page config ---
# st.set_page_config(
#     page_title="DevGuider - Developer Guide",
#     page_icon="💻",
#     layout="wide"
# )

# # --- Sidebar ---
# with st.sidebar:
#     st.title("💻 DevGuider")
#     st.markdown("**Your traditional yet modern guide to the world of coding!**")
#     st.markdown("---")

#     st.write("✨ **Quick Questions:**")
#     if st.button("📌 How do I become a frontend dev?"):
#         st.session_state.messages.append({"role": "user", "content": "How do I become a frontend developer?"})

#     if st.button("📌 Which language should I start with?"):
#         st.session_state.messages.append({"role": "user", "content": "Which programming language should I start with?"})

#     if st.button("📌 What is backend development?"):
#         st.session_state.messages.append({"role": "user", "content": "What is backend development and what should I learn?"})

#     st.markdown("---")
#     st.write("📚 **Useful Resources:**")
#     st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
#     st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
#     st.markdown("- [W3Schools](https://www.w3schools.com/)")
#     st.markdown("- [GitHub Explore](https://github.com/explore)")

#     st.markdown("---")
#     st.write("✨ *Built with ❤️ by Javeria*")

# # --- Header ---
# st.title("👨‍💻 DevGuider Chatbot")
# st.markdown("**Your trusted companion for developer careers, coding advice, and code explanations.**")

# # --- Initialize chat history ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "👋 Welcome! I’m DevGuider — your reliable companion in your programming journey. "
#                    "Ask me about coding careers, programming questions, or code explanations."
#     })

# # --- Developer keywords ---
# def is_dev_related(user_input):
#     dev_keywords = [
#         "developer", "development", "programming", "programmer",
#         "coding", "code", "python", "javascript", "frontend",
#         "backend", "fullstack", "software", "engineer", "career",
#         "web development", "app development", "AI", "ML", "roadmap",
#         "ai", "artificial intelligence", "machine learning",
#         "data science", "data analysis", "agentic ai sdk"
#     ]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in dev_keywords)

# # --- Greeting check ---
# def is_greeting(user_input):
#     greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in greetings)

# # --- Chat display ---
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # --- Chat input ---
# if prompt := st.chat_input("Type your developer question here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         thinking_placeholder = st.empty()
#         thinking_placeholder.markdown("🤔 *Thinking...*")

#     async def run_agent():
#         if is_greeting(prompt):
#             return (
#                 "👋 Hello again! I’m here to guide you with all things coding and developer careers. "
#                 "How can I help you today?"
#             )

#         if not is_dev_related(prompt):
#             return (
#                 "🙏 I apologize, but I’m designed only to guide you about developer careers, coding, "
#                 "and programming. Kindly ask something related to software development."
#             )

#         if "```" in prompt or "code" in prompt.lower():
#             instructions = (
#                 "Please clearly explain what the given code does, line by line if possible. "
#                 "Keep it simple and clear for beginners. Answer in English."
#             )
#             result = await Runner.run(
#                 assistant,
#                 prompt + "\n" + instructions,
#                 run_config=config
#             )
#             return result.final_output

#         result = await Runner.run(
#             assistant,
#             prompt,
#             run_config=config
#         )
#         return result.final_output

#     response = asyncio.run(run_agent())

#     thinking_placeholder.markdown(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})

# # --- FAQ Section ---
# with st.expander("📚 Frequently Asked Questions"):
#     st.write("**Q1:** *Is coding hard?*")
#     st.write("💬 Learning to code can feel challenging at first, but with dedication and guidance, it becomes enjoyable.")
#     st.write("**Q2:** *How long to become a developer?*")
#     st.write("💬 On average, 6 months to a year with regular practice is a good timeframe for beginners.")
#     st.write("**Q3:** *Do I need a CS degree?*")
#     st.write("💬 Not at all! Many developers are self-taught or learn through bootcamps.")
#     st.write("**Q4:** *What if I get stuck?*")
#     st.write("💬 Always ask questions, join communities, and keep experimenting — that’s the path to mastery.")












# import streamlit as st
# from dotenv import load_dotenv
# import os
# import asyncio

# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig

# load_dotenv()

# # --- Setup ---
# @st.cache_resource
# def setup():
#     MODEL_NAME = "gemini-2.0-flash"
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#     external_client = AsyncOpenAI(
#         api_key=GEMINI_API_KEY,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )

#     model = OpenAIChatCompletionsModel(
#         model=MODEL_NAME,
#         openai_client=external_client
#     )

#     config = RunConfig(
#         model=model,
#         model_provider=external_client,
#         tracing_disabled=True
#     )

#     assistant = Agent(
#         name="DevGuider",
#         instructions=(
#             "You are DevGuider, a warm, encouraging, and clear guide for aspiring developers. "
#             "You ONLY answer questions related to developer careers, programming, software engineering, "
#             "coding skills, and roadmaps. "
#             "If asked anything unrelated, politely decline and guide the user back to developer topics. "
#             "If the user provides code, always explain accurately what the code does. "
#             "If the question is asked in any language, ALWAYS reply in English."
#         )
#     )

#     return assistant, config

# assistant, config = setup()

# # --- Page Config ---
# st.set_page_config(
#     page_title="DevGuider - Developer Guide",
#     page_icon="💻",
#     layout="wide"
# )

# # --- Modern CSS ---
# st.markdown("""
#     <style>
#     body {
#         background-color: #f0f2f6;
#     }
#     .main {
#         max-width: 800px;
#         margin: auto;
#     }
#     .stChatMessage {
#         border-radius: 12px;
#         padding: 12px 16px;
#         margin: 12px 0;
#         line-height: 1.6;
#         font-family: 'Segoe UI', sans-serif;
#     }
#     .stChatMessage.user {
#         background: linear-gradient(135deg, #d1f5ff, #aee1f9);
#         text-align: right;
#     }
#     .stChatMessage.assistant {
#         background: linear-gradient(135deg, #ffffff, #e9f5e9);
#         text-align: left;
#     }
#     .stButton>button {
#         background-color: #0066cc;
#         color: #fff;
#         border: none;
#         border-radius: 8px;
#         padding: 8px 16px;
#     }
#     .stButton>button:hover {
#         background-color: #004999;
#     }
#     .block-container {
#         max-width: 800px;
#         margin: auto;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- Sidebar ---
# with st.sidebar:
#     st.title("DevGuider")
#     st.write("**Your traditional yet modern guide to the world of coding!**")
#     st.markdown("---")

#     st.write("💡 **Quick Questions:**")
#     if st.button("📌 How do I become a frontend dev?"):
#         st.session_state.messages.append({"role": "user", "content": "How do I become a frontend developer?"})
#         st.experimental_rerun()

#     if st.button("📌 Which language should I start with?"):
#         st.session_state.messages.append({"role": "user", "content": "Which programming language should I start with?"})
#         st.experimental_rerun()

#     if st.button("📌 What is backend development?"):
#         st.session_state.messages.append({"role": "user", "content": "What is backend development and what should I learn?"})
#         st.experimental_rerun()

#     st.markdown("---")
#     st.write("📚 **Helpful Resources:**")
#     st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
#     st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
#     st.markdown("- [W3Schools](https://www.w3schools.com/)")
#     st.markdown("- [GitHub Explore](https://github.com/explore)")

#     st.markdown("---")
#     st.write("✨ *Built with ❤️ by Javeria*")

# # --- Greeting ---
# st.title("💬 Developer Guider Chatbot")
# st.subheader("Welcome! Let DevGuider guide you through your programming journey.")

# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "👋 Hello! I’m DevGuider — your clear and encouraging coding guide. "
#                    "Feel free to ask anything about web development, coding careers, or code explanations!"
#     })

# # --- Keywords ---
# def is_dev_related(user_input):
#     dev_keywords = [
#         "developer", "development", "programming", "programmer",
#         "coding", "code", "python", "javascript", "frontend",
#         "backend", "fullstack", "software", "engineer", "career",
#         "web development", "app development", "AI", "ML", "roadmap", "agentic ai sdk"
#     ]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in dev_keywords)

# def is_greeting(user_input):
#     greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
#     user_input_lower = user_input.lower()
#     return any(word in user_input_lower for word in greetings)

# # --- Display Messages ---
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # --- Input ---
# if prompt := st.chat_input("Type your question about developer careers or code here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         thinking_placeholder = st.empty()
#         thinking_placeholder.markdown("🤔 *Thinking...*")

#     async def run_agent():
#         if is_greeting(prompt):
#             return (
#                 "👋 Hello! I’m DevGuider, your guide to the world of coding and developer careers. "
#                 "How may I assist you today?"
#             )

#         if not is_dev_related(prompt):
#             return (
#                 "🙏 I am sorry, but I’m only designed to guide you about developer careers, coding, "
#                 "and programming. Please ask me something related to software development!"
#             )

#         if "```" in prompt or "code" in prompt.lower():
#             instructions = (
#                 "Please clearly explain what the given code does, line by line if possible. "
#                 "Keep the answer simple and clear for a beginner. "
#                 "Always answer in English."
#             )
#             result = await Runner.run(
#                 assistant,
#                 prompt + "\n" + instructions,
#                 run_config=config
#             )
#             return result.final_output

#         result = await Runner.run(
#             assistant,
#             prompt,
#             run_config=config
#         )
#         return result.final_output

#     response = asyncio.run(run_agent())
#     thinking_placeholder.markdown(response)
#     st.session_state.messages.append({"role": "assistant", "content": response})

# # --- FAQ ---
# with st.expander("📖 Frequently Asked Questions"):
#     st.write("**Q1:** *Is coding hard?*")
#     st.write("💬 Learning to code can be challenging at first, but with practice and guidance, anyone can master it.")
#     st.write("**Q2:** *How long does it take to become a developer?*")
#     st.write("💬 It depends on your pace and focus, but 6 months to 1 year is a common range for beginners.")
#     st.write("**Q3:** *Do I need a CS degree?*")
#     st.write("💬 No! Many developers are self-taught or have bootcamp certificates.")
#     st.write("**Q4:** *What if I get stuck?*")
#     st.write("💬 Always ask questions, join communities, and keep practicing.")




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
    page_title="DevGuider - Developer Guide",
    page_icon="💻",
    layout="wide"
)

# --- Premium CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }
    .main {
        max-width: 800px;
        margin: auto;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 12px 18px;
        margin: 10px 0;
        line-height: 1.7;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .stChatMessage.user {
        background: #dbefff;
        text-align: right;
    }
    .stChatMessage.assistant {
        background: #ffffff;
        border-left: 4px solid #0d6efd;
        text-align: left;
    }
    .stButton>button {
        background: linear-gradient(135deg, #0d6efd, #66b2ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 18px;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        width: 100%;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #004999, #3399ff);
        transform: translateY(-2px);
    }
    .block-container {
        max-width: 800px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("DevGuider 🤝")
    st.write("*Your warm, professional mentor for the coding world.*")
    st.markdown("---")

    st.write("✨ **Skill Cards** — *Choose your path*")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌐 Frontend Basics"):
            st.session_state.messages.append({
                "role": "user",
                "content": "What are the basics to learn for frontend development?"
            })
            st.experimental_rerun()

        if st.button("💻 Backend Path"):
            st.session_state.messages.append({
                "role": "user",
                "content": "How should I start with backend development?"
            })
            st.experimental_rerun()

    with col2:
        if st.button("🧩 Learn Python"):
            st.session_state.messages.append({
                "role": "user",
                "content": "How do I learn Python from scratch?"
            })
            st.experimental_rerun()

        if st.button("🚀 AI & ML Guide"):
            st.session_state.messages.append({
                "role": "user",
                "content": "How do I begin with AI and Machine Learning?"
            })
            st.experimental_rerun()

    st.markdown("---")
    st.write("📚 **Useful Resources:**")
    st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/)")
    st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
    st.markdown("- [W3Schools](https://www.w3schools.com/)")
    st.markdown("- [GitHub Explore](https://github.com/explore)")

    st.markdown("---")
    st.write("✨ *Crafted with devotion by Javeria*")

# --- Greeting ---
st.title("💬 Developer Guider")
st.subheader("*A professional yet warm mentor for your development journey.*")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Greetings! I am DevGuider — your steady and clear guide for all things coding. "
                   "Feel free to ask me about developer careers, programming, or share some code for an explanation!"
    })

# --- Keyword Checks ---
def is_dev_related(user_input):
    dev_keywords = [
        "developer", "development", "programming", "programmer",
        "coding", "code", "python", "javascript", "frontend",
        "backend", "fullstack", "software", "engineer", "career",
        "web development", "app development", "AI", "ML", "roadmap", "agentic ai sdk"
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
if prompt := st.chat_input("Ask your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("⏳ *Thinking carefully...*")

#     async def run_agent():
#         if is_greeting(prompt):
#             return (
#                 "👋 Hello once more! I am here to humbly assist you with any coding or developer career query you have."
#             )
#         if not is_dev_related(prompt):
#             return (
#                 "🙏 I apologise, but I am designed exclusively to guide you about software development, "
#                 "programming, and developer careers. Kindly ask me something related."
#             )
#         if "
# " in prompt or "code" in prompt.lower():
#             instructions = (
#                 "Please explain this code thoroughly, line by line if helpful, "
#                 "keeping it easy for a beginner. Respond only in English."
#             )
#             result = await Runner.run(
#                 assistant,
#                 prompt + "\n" + instructions,
#                 run_config=config
#             )
#             return result.final_output

#         result = await Runner.run(
#             assistant,
#             prompt,
#             run_config=config
#         )
#         return result.final_output

#     response = asyncio.run(run_agent())
#     thinking_placeholder.markdown(response)
#     st.session_state.messages.append({"role": "assistant", "content": response})

# # --- FAQ Section ---
# with st.expander("📖 Frequently Asked Questions"):
#     st.write("**❓ Is coding difficult?**  \n💬 It feels challenging initially, but with steady practice and guidance, you shall overcome every hurdle.")
#     st.write("**⏳ How long to become a developer?**  \n💬 Typically 6–12 months with focus, practice and patience.")
#     st.write("**🎓 Do I need a computer science degree?**  \n💬 Not at all — dedication, practical skills, and portfolio matter more.")
#     st.write("**🆘 What if I feel stuck?**  \n💬 Always ask for help, break problems down, and trust your learning path.")
