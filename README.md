LangChain Agent with Persistent Memory (Mem0) and Tooling

An industry-grade LangChain application that demonstrates how to build a tool-augmented AI agent with persistent long-term memory, external API integrations, and robust logging.

This project showcases best practices for:

Stateless agent invocation with stateful behavior via external memory

Secure credential handling

Modular tool design

Production-ready logging and error handling

Interactive and scripted execution modes

🚀 Key Features
🧠 Persistent Memory with Mem0

Long-term memory across conversations

Semantic memory retrieval based on user queries

Graceful degradation when memory is unavailable

Memory-augmented system prompt injection

🤖 Tool-Driven Agent Intelligence

The agent automatically selects and uses tools for:

Safe arithmetic evaluation

Date calculations

Text analysis (statistics + sentiment)

Live weather data with practical recommendations

🔐 Secure Credential Management

API keys loaded from environment variables or .env

Required credentials validated at startup

Optional dependencies fail gracefully

Secrets are never hard-coded

📜 Enterprise-Grade Logging

Rotating log files with retention

Console + file logging

Structured log formatting

Debug-friendly traceability

💬 Multiple Execution Modes

Interactive REPL-style chat

Predefined example queries for testing and demos

🛠️ Technology Stack

Python 3.10+

LangChain

Google Gemini (via langchain-google-genai)

Mem0 (Persistent Memory Store)

OpenWeatherMap API

python-dotenv

AST-based safe expression evaluation

📦 Dependencies
langchain==1.2.0
langchain-google-genai==4.1.2
mem0ai==1.0.1
python-dotenv==1.2.1

🔑 Environment Variables

Create a .env file (never commit it) and define:

GEMINI_API_KEY=your_google_gemini_api_key
WEATHER_API_KEY=your_openweathermap_api_key
MEM0_API_KEY=your_mem0_api_key
🧩 Agent Capabilities
Supported Tools
1. Safe Math Calculator

Evaluates arithmetic expressions using restricted AST parsing

Prevents arbitrary code execution

Example

(234 * 12) + 98

2. Date Utility

Calculates dates relative to today

Accepts positive or negative day offsets

3. Text Analysis

Word count

Character count

Naive sentiment detection (Positive / Negative / Neutral)

4. Weather Lookup

Live temperature (°C)

Weather condition description

Practical recommendations (e.g., clothing advice)

🧠 Memory Design
How Memory Works

User sends a query

Relevant past memories are retrieved from Mem0

Memories are injected into the system prompt

Agent generates a response

The interaction is persisted for future use

Memory Rules

Memory retrieval is skipped for very short inputs (e.g., greetings)

Memory is user-scoped via a USER_ID

The agent never claims lack of context if memory exists

🧪 Example Queries Included

Arithmetic reasoning

Multi-tool orchestration (math + date)

Weather lookup with recommendations

These are useful for:

Smoke testing

Demonstrations

Regression checks

▶️ Running the Application

Start the application:

python main.py


You will be prompted to choose:

1. Interactive Chat
2. Run Example Queries

Interactive Mode

Continuous conversation

Persistent memory across turns

Exit with: exit, quit, or bye

📊 Logging

Logs are written to agent_app.log

Automatic rotation (5MB per file, 5 backups)

Console output shows concise INFO-level logs

File logs include timestamps, line numbers, and context

🔒 Security Best Practices

No credentials in source code

.env files excluded from version control

API failures handled gracefully

No use of eval() or unsafe execution paths

🧱 Design Philosophy

Stateless execution, stateful experience

Tools are authoritative

Errors are visible, not silent

Human-readable outputs, machine-safe internals

👤 Default User Identity

A default user identifier is used for memory isolation:

USER_ID = "Pushap"


This can be changed to support multi-user systems.

📈 Production Readiness

This project is suitable as:

A reference LangChain architecture

A base for enterprise assistants

A demonstration of memory-augmented LLM systems

A teaching example for tool-driven agents
