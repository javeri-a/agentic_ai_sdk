
import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)


career_agent = Agent(
    name="CareerGuruAI",
    instructions="""
You are an expert career counselor for students who have completed Matric (10th grade).
Ask structured questions to understand:
- Interest
- Strengths
- Academic preference (Theory/Practical)
- Career dreams
- Personality

Use this to recommend FSC, ICS, ICom, DAE, etc.

Always explain WHY a field is good for the student in simple words (Urdu-English mix).
NEVER answer anything outside education.

If off-topic, say: "Main sirf career guide hoon after Matric. Aap education se related poochein."

Structure:
- Greet
- Ask questions one by one
- After 5 answers, suggest path with reasons
""",
    model=model
)


user_answers = {}
questions = [
    "1️⃣ Aapko sab se zyada interest kis subject mein hai? (Bio, Math, Computer, Accounts?)",
    "2️⃣ Kis subject mein aapke marks highest thay?",
    "3️⃣ Aap zyada theory pasand karte hain ya practical kaam?",
    "4️⃣ Aap future mein kis type ka career chahte hain? (doctor, engineer, business, teacher, etc.)",
    "5️⃣ Aapko kis type ka kaam boring lagta hai?"
]

@cl.on_chat_start
async def start():
    user_answers.clear()
    await cl.Message(content="""
🎓 *Welcome to CareerGuruAI* – Matric ke baad aap ka guide!

Main aap se 5 sawalat poochunga taake main aap ki interest, strength aur aim samajh sakun.

Us ke baad main aap ko best stream recommend karunga (FSC, ICS, ICom, DAE).

Aayiye shuru karte hain...
""").send()
    await cl.Message(content=questions[0]).send()

@cl.on_message
async def on_msg(msg: cl.Message):
    user_input = msg.content.strip()

    if user_input.lower() == "restart":
        user_answers.clear()
        await cl.Message(content="🔄 Session restart ho gaya. Chaliye dobara shuru karte hain.").send()
        await cl.Message(content=questions[0]).send()
        return

    q_index = len(user_answers)

    if q_index < len(questions):
        user_answers[f"Q{q_index+1}"] = user_input
        if q_index + 1 < len(questions):
            await cl.Message(content=questions[q_index + 1]).send()
        else:
            summary = "\n".join(
                [f"{questions[i]} {user_answers[f'Q{i+1}']}" for i in range(len(questions))]
            )
            final_prompt = f"""
Student ke answers:

{summary}

In jawabat ko dekh kar suggest kijiye:
1. Konsi stream best hai (FSC, ICS, DAE, ICom)?
2. Kyun wo field unke liye best hai?
3. Career options kya milenge?
Simple Urdu-English mein jawab dein, friendly tone mein.
"""
            await cl.Message(content="🧠 Analyzing your answers...").send()
            result = await Runner.run(career_agent, final_prompt)
            await cl.Message(content="✅ Recommendation Ready!").send()
            await cl.Message(content=result.final_output).send()
            await cl.Message(content="🔁 Type `restart` agar aap dobara try karna chahte hain.").send()
    else:
        await cl.Message(content="👋 Type `restart` to begin again.").send()
