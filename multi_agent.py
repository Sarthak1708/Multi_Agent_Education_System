# multi_agent.py

import os

# Disable telemetry to avoid signal/thread errors
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

# Set Gemini API Key (better to store in environment variable)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAFNoA2TT5PLQM3ZzetvIgIjOPSV4qnH4E"

from crewai import Agent, Task, Crew, Process

MODEL = "gemini/gemini-2.5-flash"


def run_education_system(topic: str):
    """
    Runs the Multi-Agent Education System
    Returns structured study notes
    """

    # Researcher Agent
    researcher = Agent(
        role="Education Researcher",
        goal="Research educational topics",
        backstory="Expert academic researcher",
        verbose=False,
        allow_delegation=False,
        llm=MODEL
    )

    # Writer Agent
    writer = Agent(
        role="Education Content Writer",
        goal="Create structured study notes",
        backstory="Expert teacher",
        verbose=False,
        allow_delegation=False,
        llm=MODEL
    )

    # Research Task
    research_task = Task(
        description=f"""
        Research topic: {topic}

        Provide:
        - Definition
        - Explanation
        - Key points
        - Examples
        - Applications
        """,
        expected_output="Complete research data",
        agent=researcher
    )

    # Writing Task
    writing_task = Task(
        description=f"""
        Create structured study notes on {topic}

        Include:
        - Definition
        - Explanation
        - Key points
        - Examples
        - Summary
        """,
        expected_output="Structured study notes",
        agent=writer
    )

    # Crew Setup
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential
    )

    # Run Crew
    result = crew.kickoff()

    return result
