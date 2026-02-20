High Level Design (HLD)

Agentic AI – Multi-Agent Education System

1. Project Overview
The Agentic AI Education System is a multi-agent application built using CrewAI and Python.
The system takes an educational topic as input and automatically generates structured study notes using multiple AI agents working together.
Instead of using a single LLM call, the system follows an agent-based workflow where different agents perform different responsibilities such as research and content writing.
The system uses the Google Gemini 2.0 Flash model accessed via the OpenRouter API gateway.


2. System Architecture

Architecture Type:
Multi-Agent Sequential Architecture

Architecture Flow:
User Input
→ CrewAI Orchestrator
→ Researcher Agent
→ Writer Agent
→ OpenRouter API
→ Google Gemini Model
→ Structured Study Notes Output


3. Technology Stack

Backend
Python

Agent Framework
CrewAI

LLM Gateway
OpenRouter API

Language Model
Google Gemini 2.0 Flash

Environment Management
Environment Variables (.env)


4. System Components

4.1 User Interface Layer
Accepts topic input
Displays structured notes output
(Example: Streamlit or CLI)

4.2 Multi-Agent Layer (CrewAI)
This layer defines intelligent agents.

Agents used:

Education Researcher Agent
Role: Research topic
Goal: Collect detailed academic information
Output: Research content

Education Content Writer Agent
Role: Create structured study notes
Goal: Convert research into organized format
Output: Final structured notes

Process Type: Sequential (Research first → Writing second)

4.3 Task Management Layer
Two tasks are defined:

Research Task
Definition
Explanation
Key Points
Examples
Applications

Writing Task
Structured notes
Definition
Explanation
Key Points
Examples
Summary

Tasks are executed in sequential order.

4.4 LLM Integration Layer
The system does not directly call Gemini API.
Instead, it uses:
CrewAI → OpenRouter API → Google Gemini 2.0 Flash Model

OpenRouter acts as a gateway that provides access to multiple LLMs through a unified API format.

Model Used: openrouter/google/gemini-2.0-flash-exp

Benefits:
Flexibility to switch models in future
Standardized API format
Centralized LLM management


5. Workflow Execution
Step 1: User enters topic
Step 2: CrewAI initializes agents
Step 3: Researcher agent generates detailed research
Step 4: Writer agent converts research into structured notes
Step 5: Output is returned to user


6. Data Flow
Input: Educational Topic (String)
Processing:
Task decomposition
Agent execution
LLM reasoning via OpenRouter
Response formatting
Output: Structured Study Notes (Text)


7. External Integrations
OpenRouter API (LLM Gateway)
Google Gemini 2.0 Flash (Underlying LLM)
Environment Variables Used:
OPENROUTER_API_KEY
OPENAI_API_BASE
OPENAI_API_KEY
API keys are managed using environment variables for security.


8. Security Considerations
API keys are stored in environment variables
No hardcoded credentials in production
Telemetry disabled to avoid thread issues
Secure API communication via HTTPS


9. Scalability Considerations
The system can be extended by:
Adding more agents (Quiz Generator, Doubt Solver, Summary Agent)
Switching LLM models via OpenRouter without code changes
Adding database for saving generated notes
Deploying on cloud platforms
