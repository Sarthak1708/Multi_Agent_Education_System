import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
CREWAI_DISABLE_TELEMETRY = os.getenv("CREWAI_DISABLE_TELEMETRY")

os.environ["OPENAI_API_KEY"] = OPENROUTER_API_KEY
os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE
os.environ["CREWAI_DISABLE_TELEMETRY"] = CREWAI_DISABLE_TELEMETRY

from crewai import Agent, Task, Crew, Process


MODEL = "openrouter/google/gemini-2.0-flash-exp"


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
