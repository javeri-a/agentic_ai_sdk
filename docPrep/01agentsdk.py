#openai documentation intro code using OpenAI SDK

from agents import Runner , Agent

agent = Agent(name = "intro", instructions = "You are an agent that introduces itself and explains its purpose of  Openai Agentic Ai Sdk.")

result = Runner.run_sync(agent,"What is Agentic ai?")
print(result.final_output)




from agents import Runner, Agent

agent = Agent(name="my Assistant", instruction = "yuor work to resolve queries and provide information about OpenAI SDK.")
result = Runner.run_sync(agent, "What is OpenAI SDK?")
print(result.final_output)





#1st class code using gemini-2.0-flash model with OpenAI SDK because it is free.
from dotenv import load_dotenv
import os
import asyncio
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
load_dotenv()

async def main():
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
        name="Assistant",
        instructions="Your job is to resolve queries",
        model=model
    )   

    result = await Runner.run(assistant, "tell me something interesting about openai sdk.", run_config=config)
    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())