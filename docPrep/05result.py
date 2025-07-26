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






    import asyncio
from agents import Agent, Runner, SQLiteSession

async def main():
    agent = Agent(name="FixBot")
    session = SQLiteSession("correction_test")

    result = await Runner.run(agent, "What's 5 + 5?", session=session)
    print("User: What's 5 + 5?")
    print("Assistant:", result.final_output)

    # Ghalti sudharnay ke liye undo
    await session.pop_item()  # assistant response
    await session.pop_item()  # user input

    result = await Runner.run(agent, "What's 5 + 7?", session=session)
    print("User: What's 5 + 7?")
    print("Assistant:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())