#_____________________________________________________________
#                   Function Tool
#_____________________________________________________________

from agents import Agent, model_settings , function_tool

@function_tool
def weather(city:str):
    return f"The weather in {city} is sunny with a high of 25°C."

agent = Agent(
    name= "Weather Agent",
    instructions="You are an agent that provides weather information.",
    tools=[weather],
    model= "03-mini"
)


from agents import function_tool

@function_tool
def chef(recipe_name: str):
    return f"The recipe for {recipe_name} is: ..."

agent  = Agent(
    name = "Chef Agent",
    instructions="You are an agent that provides cooking recipes.",
    tools=[chef],
    model="03-mini"
)


#_____________________________________________________________
#                   Handsoff
#_____________________________________________________________

booking_agent = Agent(
    name="Booking agent",
    instructions="You are an agent that handles booking requests."
)
refund_agent = Agent(
    name="Refund agent",
    instructions="You are an agent that handles refund requests."
)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions."
        "If they ask about booking, handoff to the booking agent."
        "If they ask about refunds, handoff to the refund agent."
    ),
    handoffs=[booking_agent, refund_agent],
)

#_____________________________________________________________
#             Contextual Agent
#_____________________________________________________________


@function_tool
def suggest_discount(is_pro_user: bool) -> str:
    if is_pro_user:
        return "Aap ko 20% Pro discount milay ga."
    else:
        return "Aap ke liye standard 5% discount hai."
#_____________________________________________________________
#                  Context Class
#_____________________________________________________________
from dataclasses import dataclass
@dataclass
class UserContext:
    uid: str
    name: str
    is_pro_user: bool

    # Dummy method for demonstration
    def greet(self) -> str:
        return f"Assalamualaikum {self.name}! Aap ka ID: {self.uid}."



# ------------ 📌 4) Agent Definition ------------
def dynamic_instructions(context, agent) -> str:
    """
    Har run pe instructions banain jo user ka naam aur Pro status ka zikar karein.
    """
    greeting = context.context.greet()
    pro_status = "Pro user hain" if context.context.is_pro_user else "Pro user nahi hain"
    return f"{greeting} Aap {pro_status}. Agar discount chahiye to tool chalao."


agent = Agent[UserContext](
    name="Shopping Assistant",
    instructions=dynamic_instructions,
    tools=[suggest_discount],
)

# ------------ 📌 5) Runner Call Example ------------
# Normally, yeh run() kisi framework se call hota hai.
# Yahan sirf samjhane ke liye pseudo-call likh rahe hain.

# Example context bana lo:
context = UserContext(
    uid="U123",
    name="Javeria",
    is_pro_user=True
)

# Ab agent ko run karna:
# Pseudo-code:
# result = await Runner.run(agent, context=context, input="Mujhe discount do")

# Aap framework ke hisaab se `Runner` ka async run method use karein.