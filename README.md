🧠 LangChain Agent with Persistent Memory (Mem0)

A modular, production-grade AI agent built using LangChain, enhanced with long-term memory via Mem0, and equipped with multiple tools such as math evaluation, text analysis, date utilities, and live weather retrieval.

This project demonstrates how to build stateful AI systems while keeping the agent itself stateless, secure, and scalable.

✨ Features
🤖 LangChain Agent

Tool-calling capable agent

Clean separation of agent logic and tools

Memory-augmented system prompt

🧠 Persistent Memory (Mem0)

Stores user–assistant interactions

Retrieves relevant historical context

Optional memory layer (graceful degradation if disabled)

🛠️ Built-in Tools

Math Calculator – AST-based safe arithmetic (no eval)

Text Analysis – word count, character count, sentiment

Date Utility – relative date calculation

Weather Tool – live weather via OpenWeatherMap API

🔐 Secure Credential Management

Environment-variable based secrets

.env file support

Fail-fast validation for required keys

📜 Production-Grade Logging

Structured logging across all modules

Tool-level observability

Full traceback logging for debugging

🧪 Multiple Execution Modes

Interactive chat with persistent memory

Example/demo query execution

⚙️ Setup Instructions
1️⃣ Clone the Repository

git clone <repository-url>
cd <project-directory>

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate (Linux / macOS)
venv\Scripts\activate (Windows)

3️⃣ Install Dependencies

pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the project root with the following:

GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_openweather_api_key
MEM0_API_KEY=your_mem0_api_key (Optional)

Credential Rules

GEMINI_API_KEY → Required (LLM access)

WEATHER_API_KEY → Required (Weather API)

MEM0_API_KEY → Optional (Persistent memory)

If MEM0_API_KEY is missing, the application continues without memory.

🚀 Running the Application

Run the application using:

python main.py

You will be prompted to choose a mode:

Interactive Chat (recommended)

Run Example Queries

💬 Interactive Chat Mode

Continuous conversation with long-term memory

Clean exit commands:

exit

quit

bye

q

Informational command:

clear → shows number of turns

Each interaction is stored and reused intelligently

Example interaction:

You: What is my name?
Agent: Your name is Pushap.

🧪 Example Query Mode

Runs predefined demo scenarios demonstrating:

Mathematical reasoning

Multi-tool orchestration

External API usage (Weather)

Useful for:

Demos

Smoke testing

Debugging integrations

🛡️ Security & Design Principles

No hardcoded secrets

No use of eval()

AST-based safe computation

Time-bounded API requests

Graceful error handling

Stateless agent with external memory

Optional dependencies handled cleanly

📌 Tech Stack

Python 3.10+

LangChain

Mem0

Gemini (LLM)

OpenWeatherMap API

dotenv

requests

logging

🔮 Future Enhancements

Async agent & tools

Vector tuning for memory retrieval

API caching & rate limiting

CLI flags (argparse / typer)

Unit & integration tests

Web UI (FastAPI / Streamlit)
