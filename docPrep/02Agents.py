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