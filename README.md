This repository demonstrates the implementation of LangChain tool-based agents using Google Gemini models. The project showcases how Large Language Models (LLMs) can dynamically choose and invoke single tools, multiple tools, and API-based tools to solve diverse user queries.

🎯 Project Objective

The goal of this assignment is to:

Understand LangChain Agents and their architecture

Implement custom tools in LangChain

Explore single-tool and multi-tool agent behavior

Integrate external APIs with LLMs

Learn practical agent orchestration using Google Gemini

🧠 Agents Implemented
1️⃣ Single Tool Agent

Uses one tool only

Suitable for focused tasks such as:

Mathematical calculations

Simple deterministic operations

2️⃣ Multi Tool Agent

Uses multiple tools

The LLM dynamically decides which tool to invoke based on user intent

Handles diverse queries such as:

Calculations

Date operations

Text analysis

3️⃣ API Agent

Integrates external APIs with the LLM

Demonstrates real-world data access

Example:

🌦️ Weather information retrieval using OpenWeatherMap API

🛠️ Tech Stack

Language: Python 3.10+

Framework: LangChain

LLM: Google Gemini

gemini-2.5-flash

gemini-2.5-flash-lite

Environment: Virtual Environment (venv)

External API: OpenWeatherMap

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/hemant-crossml/Langchain_Assignment.git
cd Langchain_Assignment
2️⃣ Create & Activate Virtual Environment
python -m venv myenv


# Linux / macOS
source myenv/bin/activate


# Windows
myenv\Scripts\activate
🔐 API Key Configuration

Add your Google Gemini API key in cred.py:

gemini_api_key = "YOUR_GEMINI_API_KEY"

⚠️ Important

Never commit real API keys to GitHub

For production projects, use .env files and environment variables

If using the Weather API Agent, ensure your OpenWeatherMap API key is also properly configured.

▶️ How to Run

Run the main application:

python main.py

The agent will:

Understand the user query

Select the appropriate tool

Execute the tool

Return the final response

💡 Example Use Cases

➗ Solve mathematical calculations

📅 Find future or past dates

📝 Analyze or transform text content

🌦️ Fetch real-time weather information

🧠 Dynamically choose tools based on query intent

📘 Learning Outcomes

By completing this assignment, you will gain:

Practical understanding of LangChain Agents

Hands-on experience with tool invocation and orchestration

Clear insight into single-tool vs multi-tool agents

Experience integrating external APIs with LLMs

Knowledge of clean project structuring for AI applications
