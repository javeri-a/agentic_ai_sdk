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
