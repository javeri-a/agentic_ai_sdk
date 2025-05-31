
import chainlit as cl
from agent import Agent, RunConfig, Async

@cl.on_message
async def main(message: cl.Message):
    # Our custom logic goes here...
    # Send a fake response back to the user
    await cl.Message(
        content=f"message received javbot: {message.content}",
    ).send()

    print("thanks for using me")

