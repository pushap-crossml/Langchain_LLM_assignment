# LangChain Agent with Persistent Memory (Mem0) and Tooling
A production-style LangChain agent powered by Google Gemini, featuring multiple custom tools (math, dates, weather, text analysis) and Mem0 integration for long-term memory.
This project demonstrates how to build context-aware, personalized AI agents using modern LLM orchestration techniques.

## 🚀 Features
🔹 Core LLM

- Google Gemini chat models:

   - gemini-2.5-flash

   - gemini-2.5-flash-lite

🔹 LangChain Agent

  - Tool-calling agent that:

  - Iteratively selects tools

  - Executes them in a loop

  - Produces a final response based on tool outputs

🔹 Built-in Tools

 - Math Calculator

    - Safe AST-based evaluation

    - Prevents arbitrary code execution

 - Date Utility

    - Computes future or relative dates

- Weather Tool

    - Fetches real-time weather data using OpenWeatherMap API

- Text Analysis

   - Word and character count

   - Basic sentiment estimation

🔹 Mem0 Long-Term Memory

- Stores important interaction snippets

- Retrieves relevant memories using user_id

- Injects retrieved memory into the system prompt

- Enables personalized and context-aware conversations

🔹 Logging & Observability

- Console + file logging

- Log rotation enabled

- Per-module loggers for easier debugging

- Detailed traces for agent reasoning and tool usage

🔹 Interactive CLI

- Continuous chat loop with memory

- Supports both:

    - Interactive user input

    - Predefined example runs

### 🎯 Project Objective

This assignment focuses on:

- Understanding LangChain agents

- Implementing custom tools

- Exploring single-tool and multi-tool agents

- Integrating external APIs with LLMs

- Using Google Gemini for real-world agent orchestration

- Adding persistent memory using Mem0

## 🧠 Agents Implemented
1️⃣ Single Tool Agent

Uses exactly one tool

Best for focused tasks (e.g., calculations)

2️⃣ Multi Tool Agent

Uses multiple tools

LLM decides which tool(s) to call based on user intent

3️⃣ API Agent

Integrates external APIs

Example: real-time weather information retrieval

### 🧰 Tech Stack

- **Language: Python 3.10+**

- **Framework: LangChain+**

- **LLM: Google Gemini**

- **APIs:**

  - OpenWeatherMap

  - Mem0

- Environment: Python Virtual Environment (venv)

## ⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/pushap-crossml/Langchain_LLM_assignment.git
cd Assignment_Langchain

2️⃣ Create & Activate Virtual Environment
python -m venv myenv


Linux / macOS

source venv/bin/activate


Windows

venv\Scripts\activate

## 🔐 API Key Configuration

Add your API keys in cred.py:

- **gemini_api_key = "YOUR_GEMINI_API_KEY"**
- **weather_api_key = "YOUR_WEATHER_API_KEY"**
- **mem0_api_key = "YOUR_MEM0_API_KEY"**


## ▶️ How to Run

Run the main application:

python main.py


The agent will:

- Understand the user query

- Retrieve relevant memory (if available)

- Select appropriate tool(s)

- Execute tools

- Generate a final response

### 💡 Example Use Cases

- Solve mathematical expressions

- Calculate future dates

- Analyze text content

- Fetch real-time weather data

- Dynamically choose tools based on query intent

- Personalize responses using stored memory

### 📚 Learning Outcomes

By completing this project, you will:

- Learn how to wire a Gemini-powered LangChain agent

- Design and register reusable custom tools

- Implement single-tool and multi-tool agent workflows

- Integrate external APIs into LLM-driven systems

- Build a long-term memory layer using Mem0:

   - Store structured interactions

   - Retrieve memories per user

   - Inject memory into prompts

- Create an interactive CLI agent

- Apply best practices for:

    - Logging

    - Error handling

    - Environment-based configuration

    - Production-style project design
