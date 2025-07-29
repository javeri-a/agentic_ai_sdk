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









    # loop_chat.py
import asyncio
from agents import Agent, Runner, SQLiteSession

async def main():
    agent = Agent(name="LoopBot", instructions="Be helpful and brief.")
    session = SQLiteSession("loop_user")

    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = await Runner.run(agent, user_input, session=session)
        print("Assistant:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())





# 05result.py
from agents import Runner,Agent, Message , ToolCallItem, StringOutput

class SummaryAgent(Agent):
    def describe(self):
        return {
            "name": "summary_agent",
            "description": "Summarizes a given paragraph in 1 line",
        }
    
    def generate(self, messages, tools, config):
        input_text = messages[-1].content
        # Fake summary logic (replace with actual summarization tool if needed)
        summary = f"Summary: {input_text[:30]}..."
        return [Message.from_assistant(summary)]
    
    runner = Runner(agents=[SummaryAgent()])

# Step 3: Run the agent
result = runner.run("Yeh aik lambi kahani hai jismein aik larka sheher jata hai...")

# Step 4: Access final_output
print("\n✅ Final Output:")
print(result.final_output)  # Could be string or output_type object

# Step 5: Access new_items (All steps by agent)
print("\n🧩 New Items:")
for item in result.new_items:
    print(f"- {item.__class__.__name__}: {item.raw}")

# Step 6: Create next input from this result
next_input = result.to_input_list()
print("\n🔁 Next Input List:")
for i in next_input:
    print("-", i.content if hasattr(i, "content") else i)

# Step 7: See which agent handled this
print("\n🧑‍💼 Last Agent:")
print(result.last_agent.describe()["name"])

# Step 8: Guardrail results
print("\n🛡️ Input Guardrails:")
print(result.input_guardrail_results)

print("\n🛡️ Output Guardrails:")
print(result.output_guardrail_results)

# Step 9: Raw LLM responses (debug info)
print("\n🧾 Raw Responses:")
print(result.raw_responses)

# Step 10: Original input
print("\n📥 Original Input:")
print(result.input)
from agents import Runner,Agent, Message , ToolCallItem, StringOutput

class SummaryAgent(Agent):
    def describe(self):
        return {
            "name": "summary_agent",
            "description": "Summarizes a given paragraph in 1 line",
        }
    
    def generate(self, messages, tools, config):
        input_text = messages[-1].content
        # Fake summary logic (replace with actual summarization tool if needed)
        summary = f"Summary: {input_text[:30]}..."
        return [Message.from_assistant(summary)]
    
    runner = Runner(agents=[SummaryAgent()])

# Step 3: Run the agent
result = runner.run("Yeh aik lambi kahani hai jismein aik larka sheher jata hai...")

# Step 4: Access final_output
print("\n✅ Final Output:")
print(result.final_output)  # Could be string or output_type object

# Step 5: Access new_items (All steps by agent)
print("\n🧩 New Items:")
for item in result.new_items:
    print(f"- {item.__class__.__name__}: {item.raw}")

# Step 6: Create next input from this result
next_input = result.to_input_list()
print("\n🔁 Next Input List:")
for i in next_input:
    print("-", i.content if hasattr(i, "content") else i)

# Step 7: See which agent handled this
print("\n🧑‍💼 Last Agent:")
print(result.last_agent.describe()["name"])

# Step 8: Guardrail results
print("\n🛡️ Input Guardrails:")
print(result.input_guardrail_results)

print("\n🛡️ Output Guardrails:")
print(result.output_guardrail_results)

# Step 9: Raw LLM responses (debug info)
print("\n🧾 Raw Responses:")
print(result.raw_responses)

# Step 10: Original input
print("\n📥 Original Input:")
print(result.input)
class SummaryAgent(Agent):
    def describe(self):
        return {
            "name": "summary_agent",
            "description": "Summarizes a given paragraph in 1 line",
        }
    
    def generate(self, messages, tools, config):
        input_text = messages[-1].content
        # Fake summary logic (replace with actual summarization tool if needed)
        summary = f"Summary: {input_text[:30]}..."
        return [Message.from_assistant(summary)]
    
    runner = Runner(agents=[SummaryAgent()])

# Step 3: Run the agent
result = runner.run("Yeh aik lambi kahani hai jismein aik larka sheher jata hai...")

# Step 4: Access final_output
print("\n✅ Final Output:")
print(result.final_output)  # Could be string or output_type object

# Step 5: Access new_items (All steps by agent)
print("\n🧩 New Items:")
for item in result.new_items:
    print(f"- {item.__class__.__name__}: {item.raw}")

# Step 6: Create next input from this result
next_input = result.to_input_list()
print("\n🔁 Next Input List:")
for i in next_input:
    print("-", i.content if hasattr(i, "content") else i)

# Step 7: See which agent handled this
print("\n🧑‍💼 Last Agent:")
print(result.last_agent.describe()["name"])

# Step 8: Guardrail results
print("\n🛡️ Input Guardrails:")
print(result.input_guardrail_results)

print("\n🛡️ Output Guardrails:")
print(result.output_guardrail_results)

# Step 9: Raw LLM responses (debug info)
print("\n🧾 Raw Responses:")
print(result.raw_responses)

# Step 10: Original input
print("\n📥 Original Input:")
print(result.input)
class SummaryAgent(Agent):
    def describe(self):
        return {
            "name": "summary_agent",
            "description": "Summarizes a given paragraph in 1 line",
        }
    
    def generate(self, messages, tools, config):
        input_text = messages[-1].content
        # Fake summary logic (replace with actual summarization tool if needed)
        summary = f"Summary: {input_text[:30]}..."
        return [Message.from_assistant(summary)]
    
    runner = Runner(agents=[SummaryAgent()])

# Step 3: Run the agent
result = runner.run("Yeh aik lambi kahani hai jismein aik larka sheher jata hai...")

# Step 4: Access final_output
print("\n✅ Final Output:")
print(result.final_output)  # Could be string or output_type object

# Step 5: Access new_items (All steps by agent)
print("\n🧩 New Items:")
for item in result.new_items:
    print(f"- {item.__class__.__name__}: {item.raw}")

# Step 6: Create next input from this result
next_input = result.to_input_list()
print("\n🔁 Next Input List:")
for i in next_input:
    print("-", i.content if hasattr(i, "content") else i)

# Step 7: See which agent handled this
print("\n🧑‍💼 Last Agent:")
print(result.last_agent.describe()["name"])

# Step 8: Guardrail results
print("\n🛡️ Input Guardrails:")
print(result.input_guardrail_results)

print("\n🛡️ Output Guardrails:")
print(result.output_guardrail_results)

# Step 9: Raw LLM responses (debug info)
print("\n🧾 Raw Responses:")
print(result.raw_responses)

# Step 10: Original input
print("\n📥 Original Input:")
print(result.input)