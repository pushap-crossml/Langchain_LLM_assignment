# Langchain_LLM_assignment
# LangChain Agent Demo

This project demonstrates how Google Gemini models can power LangChain agents to intelligently select and use tools or APIs to handle user queries.

---

## 🎯 Project Goals

The main objectives of this assignment are to:

- Gain practical experience with LangChain agents  
- Build and integrate custom tools  
- Explore agents with single or multiple tools  
- Connect external APIs to LLMs  
- Learn real-world orchestration of AI agents using Google Gemini  

---

## 🧠 Implemented Agent Types

### 1️⃣ Focused Tool Agent
- Works with a **single tool**  
- Ideal for specific tasks like calculations  

### 2️⃣ Multi-Tool Intelligence Agent
- Capable of using **multiple tools**  
- Automatically decides which tool to call based on user intent  

### 3️⃣ API-Connected Agent
- Fetches dynamic data via **external APIs**  
- Example: retrieving live weather information  

---

## 🛠️ Technology Stack

- **Language:** Python 3.10+  
- **Framework:** LangChain  
- **LLM:** Google Gemini (gemini-3-flash-preview)  
- **Environment:** Virtual Environment (`myenv`)  
- **API:** OpenWeatherMap  

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

git clone https://github.com/pushap-crossml/Langchain_LLM_assignment.git
cd Assignment_Langchain
Step 2: Set Up Virtual Environment

python -m venv myenv
source myenv/bin/activate  # Linux / macOS
myenv\Scripts\activate     # Windows
Step 3: Configure API Key
Add your Gemini API key in cred.py:

gemini_api_key = "YOUR_GEMINI_API_KEY"

▶️ Running the Application

python main.py
Workflow:

Understand the user query

Select the appropriate tool

Execute the tool

Return the final result

📌 Sample Use Cases
Solve arithmetic problems

Calculate or predict future dates

Analyze and process text

Fetch live weather data

Dynamically select tools based on query intent

💡 What You’ll Learn
How LangChain agents work in practice

Tool selection and orchestration

Differences between single-tool and multi-tool agents

API integration with LLMs

Organizing AI projects effectively

