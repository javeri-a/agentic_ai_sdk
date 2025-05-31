import chainlit as cl
import google.generativeai as genai
import os

# Set API key from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

@cl.on_message
async def main(message: cl.Message):
    response = model.generate_content(message.content)
    await cl.Message(content=response.text).send()
