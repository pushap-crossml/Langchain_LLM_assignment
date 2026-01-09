LangChain Agent Demo

Demonstrates how Google Gemini models power LangChain agents

Agents intelligently select and use tools or APIs

Handles diverse user queries through dynamic tool orchestration

🎯 Project Goals

Gain hands-on experience with LangChain agents

Build and integrate custom tools

Explore single-tool and multi-tool agent architectures

Connect external APIs with LLMs

Learn real-world AI agent orchestration using Google Gemini

🧠 Implemented Agent Types
1️⃣ Focused Tool Agent

Uses a single dedicated tool

Best suited for:

Mathematical calculations

Specific, well-defined tasks

2️⃣ Multi-Tool Intelligence Agent

Uses multiple tools

Automatically:

Understands user intent

Selects the appropriate tool

Executes the required operation

3️⃣ API-Connected Agent

Integrates external APIs

Fetches live, dynamic data

Example use case:

Real-time weather information retrieval

🛠️ Technology Stack

Programming Language: Python 3.10+

Framework: LangChain

LLM: Google Gemini (gemini-3-flash-preview)

Environment: Python Virtual Environment (myenv)

External API: OpenWeatherMap

⚙️ Setup Instructions
Step 1: Clone the Repository

git clone https://github.com/pushap-crossml/Langchain_LLM_assignment.git

cd Langchain_LLM_assignment

Step 2: Create & Activate Virtual Environment

python -m venv myenv

Linux / macOS: source myenv/bin/activate

Windows: myenv\Scripts\activate

Step 3: Configure API Keys

Add Gemini API key in cred.py

Example:

gemini_api_key = "YOUR_GEMINI_API_KEY"

⚠️ Never commit real API keys

Use .env files or environment variables in production

▶️ Running the Application

Run the main program:

python main.py

Application Workflow

Parse and understand the user query

Identify the required tool

Execute the selected tool

Return the final response to the user

📌 Sample Use Cases

Solve arithmetic expressions

Calculate or predict future dates

Analyze and process text inputs

Retrieve live weather data

Dynamically select tools based on query intent

💡 What You’ll Learn

Practical implementation of LangChain agents

Tool selection and orchestration strategies

Differences between single-tool and multi-tool agents

Integrating APIs with large language models
