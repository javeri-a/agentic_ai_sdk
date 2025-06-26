
import os
import chainlit as cl
from dotenv import load_dotenv
from agents import (
    RunConfig, 
    AsyncOpenAI, 
    OpenAIChatCompletionsModel, 
    Agent, 
    Runner, 
    function_tool
)

# ✅ Load environment variables
load_dotenv()

# ✅ Weather tool
@function_tool
def getWeather(city: str) -> str:
    return f"The weather of {city} is moderate."

# ✅ Model and Client Config
MODEL_NAME = "gemini-2.0-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
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

# ✅ Agent setup
assistant = Agent(
    name="Weather Agent",
    instructions="Only answer weather-related queries.",
    model=model,
    tools=[getWeather]
)

# ✅ Greet user when chat starts
@cl.on_chat_start
async def start_chat():
    await cl.Message(
        author="Weather Agent",
        content="🌤️ *Welcome!* Ask me about the weather in any city."
    ).send()

# ✅ Handle messages from user
@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message(content="⏳ *Thinking...*").send()

    result = await Runner.run(
        starting_agent=assistant,
        input=message.content,
        run_config=config
    )

    await cl.Message(
        content=f"✅ **Result:**\n{result.final_output}"
    ).send()
