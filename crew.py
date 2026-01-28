import os
# Set Groq API key
os.environ["GROQ_API_KEY"] = "api_key_here"  # Replace with your actual Groq API key
from crewai import Agent, Task, Crew
print(os.getenv("GROQ_API_KEY")) 
assistant = Agent(
    role="Python assistant",
    goal="Print Hello world",
    backstory="You help users to write and run basic python code",
    llm="groq/llama-3.1-8b-instant",  # ✅ FIXED MODEL
    verbose=True
)

philospher = Agent(
    role="Philospher",
    goal="Share the meaning of life from literature",
    backstory="You are inspired by the Hitchhiker's Guide to the Galaxy",
    llm="groq/llama-3.1-8b-instant",  # ✅ FIXED MODEL
    verbose=True
)

task1 = Task(
    description="Print Hello world in python",
    agent=assistant,
    expected_output="Hello world",
)

task2 = Task(
    description="Tell me the meaning of life according to literature",
    agent=philospher,
    expected_output="42",
)

crew = Crew(
    agents=[assistant, philospher],
    tasks=[task1, task2],
    verbose=True,
    tracing=True
)

result = crew.kickoff()
print("below is the final result from the crew")
print(result)
