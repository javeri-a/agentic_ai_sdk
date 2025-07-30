#  1️⃣ What is a Session?
# Definition:
# A Session is a memory store for an agent’s conversation.
# It keeps track of the whole chat — what the user said, what the agent replied — so the agent does not forget what was discussed before.

# Real-life example:
# Imagine you are talking to a shopkeeper about buying cloth. If you come back tomorrow, the shopkeeper remembers your measurements, color choices, and price range — so you don’t need to repeat yourself.
# That memory is your session.



#_______________________________________________________________
#             Session Example
#_______________________________________________________________

from agents import SQLiteSession

session = SQLiteSession("session_id")
session = SQLiteSession("session_id", "my_database.db")



#______________________________________________________________
#        Running an Agent with Session
#______________________________________________________________


from agents import Agent, Runner,SQLiteSession
import asyncio
agent = Agent(name = "Shopping Assistant",
              instructions = "You are a helpful shopping assistant.")
session = SQLiteSession("session_id", "my_database.db")

result = await Runner.run(
    agent, "Hello, I need help with my shopping.",
    session = session

)

print (result.final_output)


result = await Runner.run(
    agent,
    "What state is it in?",
    session=session
)
print(result.final_output) 

#_____________________________________________________________
#                Get all conversation items:
#_____________________________________________________________
# You can get all the conversation items in the session by calling the `get_conversation` method
items = await session.get_items()



#______________________________________________________________
# ➕ Add new items yourself:
#______________________________________________________________

await session.add_items([
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
])

#
#_______________________________________________________________

last_item = await session.pop_item()





async def main():
    agent = Agent (name = "Assistant")
    session = SQLiteSession("session_id", "my_database.bd")
    print("User: Where is the Golden Gate Bridge?")
    result = await Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print("Assistant:", result.final_output)

asyncio.run(main())



async def main():
    agent = Agent (name = "Assistant")
    session = SQLiteSession("session_id", "my_database.bd")
    print("User: Where is the Golden Gate Bridge?")
    result = await Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print("Assistant:", result.final_output)

asyncio.run(main())


async def main():
    agent = Agent (name = "Assistant")
    session = SQLiteSession("session_id", "my_database.bd")
    print("User: Where is the Golden Gate Bridge?")
    result = await Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print("Assistant:", result.final_output)

asyncio.run(main())



async def main():
    agent = Agent (name = "Assistant")
    session = SQLiteSession("session_id", "my_database.bd")
    print("User: Where is the Golden Gate Bridge?")
    result = await Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print("Assistant:", result.final_output)

asyncio.run(main())


async def main():
    agent = Agent (name = "Assistant")
    session = SQLiteSession("session_id", "my_database.bd")
    print("User: Where is the Golden Gate Bridge?")
    result = await Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print("Assistant:", result.final_output)

asyncio.run(main())

