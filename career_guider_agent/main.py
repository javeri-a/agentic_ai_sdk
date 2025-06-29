import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner

# Load .env file and get the API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set up the OpenAI client for Gemini model
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Choose the model to use
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Define the agent with clear rules
career_agent = Agent(
    name="CareerGuruAI",
    instructions="""
You are a career counselor for students who just finished Matric (10th grade).
Your job is to ask 5 questions:
- Their interests
- Strong subjects
- Do they like theory or practical work
- What career they dream of
- What type of work they find boring

Based on these, suggest FSC, ICS, ICom or DAE.

Always explain in simple Urdu-English why you are giving that suggestion.

If someone asks anything not about study, say:
"Main sirf career guide hoon after Matric. Aap education se related poochein."

Your steps:
1. Greet the student
2. Ask 5 questions one by one
3. Give your suggestion with reasons
"""
)

# Store user answers here
user_answers = {}

# The 5 questions you will ask
questions = [
    "1️⃣ Which subject do you like the most? (Bio, Math, Computer, Accounts?)",
    "2️⃣ In which subject did you get the highest marks?",
    "3️⃣ Do you prefer theory or practical work?",
    "4️⃣ What kind of career do you want? (doctor, engineer, business, teacher, etc.)",
    "5️⃣ What kind of work do you find boring?"
]

# Words that mean the question is off-topic
off_topic_keywords = [
    "weather", "news", "joke", "sports", "politics", "game",
    "music", "movie", "film", "travel", "food", "recipe",
    "technology", "fashion", "songs", "song"
]

@cl.on_chat_start
async def start():
    """This runs when the chat starts."""
    user_answers.clear()
    await cl.Message(content="""
🎓 *Welcome to CareerGuruAI!*  
I will help you decide what to study after Matric.

I will ask you 5 simple questions about your interests, marks, and goals.

After that, I will tell you which stream is best for you and why.

Let’s start!
""").send()
    await cl.Message(content=questions[0]).send()

@cl.on_message
async def on_msg(msg: cl.Message):
    """This runs whenever the user sends a message."""
    user_input = msg.content.strip().lower()

    # If user wants to restart
    if user_input == "restart":
        user_answers.clear()
        await cl.Message(content="🔄 Restarted. Let’s start again!").send()
        await cl.Message(content=questions[0]).send()
        return

    # If the message is off-topic
    if any(keyword in user_input for keyword in off_topic_keywords):
        await cl.Message(content="📚 *Main sirf career guide hoon after Matric. Aap education se related poochein.*").send()
        return

    # Figure out which question we are on
    q_index = len(user_answers)

    if q_index < len(questions):
        # Save the user’s answer
        user_answers[f"Q{q_index + 1}"] = msg.content.strip()

        # If there are more questions, ask next
        if q_index + 1 < len(questions):
            await cl.Message(content=questions[q_index + 1]).send()
        else:
            # All answers done — make the final prompt
            summary = "\n".join(
                [f"{questions[i]} {user_answers[f'Q{i + 1}']}" for i in range(len(questions))]
            )

            final_prompt = f"""
Here are the student’s answers:

{summary}

Based on this, please suggest:
1. Which stream is best (FSC, ICS, ICom, DAE)
2. Why it is good for them
3. What career options they can get

Answer in simple Urdu-English, friendly tone.
"""

            await cl.Message(content="🧠 Thinking about your answers...").send()
            result = await Runner.run(career_agent, final_prompt)
            await cl.Message(content="✅ *Here is my suggestion!*").send()
            await cl.Message(content=result.final_output).send()
            await cl.Message(content="🔁 Type `restart` if you want to try again.").send()
    else:
        # If all questions are done, tell them to restart if they type more
        await cl.Message(content="👋 Type `restart` to start again.").send()


