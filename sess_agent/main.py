# from agents import Agent , Runner, SQLiteSession
# import os
# import asyncio

# async def func1():

#   agent = Agent(name = "Assistant", instruction = "hr ques ka short ans dena hai")


# session = SQLiteSession("my_first_session")

# result  = await Runner.run(agent, "Golden Gate bridge kis city me h?", session = session)
# print (result.final_output)

# result = await Runner.run (agent, "kis state me h?", session  = session)
# print(result.final_output)




import asyncio
from agents import Agent, Runner,  AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
    ## Now set Api key
gemini_api_key = os.getenv("GEMINI_API_KEY")


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
    # 1️⃣ Agent banao
    agent = Agent(
        name="Assistant",
        instructions="Har sawaal ka chhota jawab dena hai."
    )

    # 2️⃣ Session banao
    session = SQLiteSession("my_first_session")

    # 3️⃣ Pehla sawaal
    result = await Runner.run(agent, "Golden Gate bridge kis city me h?", session=session)
    print(result.final_output)

    # 4️⃣ Dusra sawaal (woh yaad rakhega pehla jawab bhi)
    result = await Runner.run(agent, "Kis state me h?", session=session)
    print(result.final_output)

# 5️⃣ Async function chalane ke liye
asyncio.run(main())
