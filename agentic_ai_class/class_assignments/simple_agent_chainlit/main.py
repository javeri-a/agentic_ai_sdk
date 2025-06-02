import os
import asyncio
import chainlit as cl
from dotenv import load_dotenv

from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Agent,
    Runner,
    RunConfig
)

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  


def get_gemini_model():
    gemini_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    gemini_model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=gemini_client
    )
    gemini_config = RunConfig(
        model=gemini_model,
        model_provider=gemini_client,
        tracing_disabled=True
    )
    return gemini_model, gemini_config


def get_openai_model():
    openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    openai_model = OpenAIChatCompletionsModel(
        model="gpt-4-turbo",
        openai_client=openai_client
    )
    openai_config = RunConfig(
        model=openai_model,
        model_provider=openai_client,
        tracing_disabled=True
    )
    return openai_model, openai_config


assistant = Agent(
    name="Assistant",
    instructions="Your job is to resolve queries",
)


@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    model, config = get_gemini_model()

    for attempt in range(3):
        try:
            result = await Runner.run(assistant, user_input, run_config=config)
            await cl.Message(content=result.final_output).send()
            return
        except Exception as e:
            if "503" in str(e) and attempt < 2:
                await asyncio.sleep(2 ** attempt)  
            else:
             
                if OPENAI_API_KEY:
                    try:
                        fallback_model, fallback_config = get_openai_model()
                        fallback_result = await Runner.run(assistant, user_input, run_config=fallback_config)
                        await cl.Message(content=f"💡 (Fallback GPT-4) {fallback_result.final_output}").send()
                        return
                    except Exception as fallback_error:
                        await cl.Message(content="❗ Both Gemini and fallback GPT-4 are currently unavailable.").send()
                        return
                else:
                    await cl.Message(content="❗ The Gemini model is currently overloaded. Please try again later.").send()
                    return
