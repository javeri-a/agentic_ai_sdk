import asyncio
from agents import Agent, Runner

async def main():
    agent = Agent(
        name="SimpleBot",
        instructions="Give short, helpful answers."
    )

    result = await Runner.run(agent, "What is the capital of France?")
    print("Answer:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())











    import asyncio
from agents import Agent, Runner, SQLiteSession

async def main():
    agent = Agent(name="MemoryBot", instructions="Be concise.")
    session = SQLiteSession("memory_user")

    result = await Runner.run(agent, "Where is Mount Everest?", session=session)
    print("User: Where is Mount Everest?")
    print("Assistant:", result.final_output)

    result = await Runner.run(agent, "Which country is it in?", session=session)
    print("User: Which country is it in?")
    print("Assistant:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())