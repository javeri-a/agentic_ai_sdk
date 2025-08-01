def main():
    print("Hello from docprep!")
   
    print("User: Where is the Golden Gate Bridge?")
    result = Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)
   
    print("User: Where is the Golden Gate Bridge?")
    result = Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)
   
    print("User: Where is the Golden Gate Bridge?")
    result = Runner.run(agent, "Where is the Golden Gate Bridge?", session=session)
    print("Assistant:", result.final_output)

if __name__ == "__main__":
    main()
