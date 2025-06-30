# agent_utils.py
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import os
from dotenv import load_dotenv

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

async def run_agent(agent_instructions, prompt):
    assistant = Agent(
        name="Assistant",
        instructions=agent_instructions
    )
    result = await Runner.run(assistant, prompt, run_config=config)
    return result.final_output
