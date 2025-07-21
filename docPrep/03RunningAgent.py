# Pehle zaroori cheezein import karo
from agents import Agent, function_tool

# Hum aik tool bana rahe hain
@function_tool
def get_weather(city: str) -> str:
    # Misaal ke taur par hard coded
    return f"Mausam {city} mein dhoopdaar hai!"

# Ab agent banayein
weather_agent = Agent(
    name="Weather Assistant",
    instructions="Hamesha Urdu mein jawab do.",
    tools=[get_weather],
)

# Run karne ke liye
from agents import Runner
import asyncio

async def main():
    result = await Runner.run(weather_agent, "Karachi ka mausam kaisa hai?")
    print(result.final_output)

# Run karne ke liye
asyncio.run(main())












#______________________________________________________________
#             Dynamic Instructions
#______________________________________________________________


from dataclasses import dataclass
from agents import Agent

# Context class banai
@dataclass
class UserContext:
    uid: str
    is_pro_user: bool

# Dynamic instructions function
def dynamic_instructions(context, agent) -> str:
    if context.context.is_pro_user:
        return "Aap premium hain. Tafseel se jawab dein."
    else:
        return "Aap basic user hain. Mukhtasir jawab dein."

# Agent banayein
premium_agent = Agent[UserContext](
    name="Premium Assistant",
    instructions=dynamic_instructions,
)

from agents import Runner
import asyncio

async def main():
    context = UserContext(uid="123", is_pro_user=True)
    result = await Runner.run(premium_agent, "Mujhe kuch batao.", context=context)
    print(result.final_output)

asyncio.run(main())








#_____________________________________________________________
#             Handoffs 
#_____________________________________________________________

from agents import Agent

booking_agent = Agent(
    name="Booking",
    instructions="Booking questions handle karo.",
)

refund_agent = Agent(
    name="Refund",
    instructions="Refund questions handle karo.",
)

triage_agent = Agent(
    name="Triage",
    instructions=(
        "User ki madad karo.\n"
        "Agar booking sawaal ho toh booking_agent ko handoff karo.\n"
        "Agar refund sawaal ho toh refund_agent ko handoff karo."
    ),
    handoffs=[booking_agent, refund_agent],
)

from agents import Runner
import asyncio

async def main():
    result = await Runner.run(triage_agent, "Mujhe booking karni hai.")
    print(result.final_output)

asyncio.run(main())
