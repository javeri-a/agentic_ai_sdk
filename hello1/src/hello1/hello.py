# import os
# import  chainlit as cl
# from agents  import Agent,  RunConfig, AsynsOpenAI, OpenAIChatCompletionsModel
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# provider = AsynsOpenAI(api_key =os.getenv("GEMINI_API_KEY"))
                       
# provider =AsyncOpenAI(
#     AsynsOpenAI(
#         api_key=gemini_api_key,
#         api_base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
# )
# @cl.on.message
# async def handle_message(message: cl.Message):
#     # This function will be called when a message is received
#     await cl.Message(
#         content="Hello from the hello1 app! You sent: " + message.content
#     ).send()


import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()
