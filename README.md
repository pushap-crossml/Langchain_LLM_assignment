# LangChain Assignment: Tool-Driven AI Agents using Google Gemini

This repository demonstrates the implementation of **LangChain tool-based agents** using **Google Gemini models**.  
The project showcases how **Large Language Models (LLMs)** can dynamically choose and invoke **single tools, multiple tools, and API-based tools** to solve user queries.

---

## 📌 Project Objective

The goal of this assignment is to:

- Understand LangChain Agents  
- Implement custom tools  
- Explore single-tool vs multi-tool agents  
- Integrate external APIs with LLMs  
- Learn practical agent orchestration using Google Gemini  

---

## 🧠 Agents Implemented

### 1️⃣ Single Tool Agent
- Uses only one tool  
- Suitable for focused tasks like mathematical calculations  

### 2️⃣ Multi Tool Agent
- Uses multiple tools  
- LLM dynamically decides which tool(s) to invoke based on user intent  

### 3️⃣ API Agent
- Integrates external APIs  
- Example: Weather information retrieval using OpenWeatherMap  

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+  
- **Framework:** LangChain  
- **LLM:** Google Gemini  
  - `gemini-2.5-flash`  
  - `gemini-2.5-flash-lite`  
- **Environment:** Virtual Environment (`myenv`)  
- **External API:** OpenWeatherMap  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
- **git clone https://github.com/pushap-crossml/Langchain_LLM_Assignment.git**
- **cd Assignment_Langchain**

2️⃣ Create & Activate Virtual Environment
- **python -m venv myenv**


### Activate the environment:

Linux / macOS

- **source myenv/bin/activate**


Windows

- **myenv\Scripts\activate**

### 🔐 API Key Configuration

Add your Gemini API Key in cred.py:

- gemini_api_key = "YOUR_GEMINI_API_KEY"
- open_weather_Map ="YOUR_WEATHER_MAP_KEY"

### ▶️ How to Run

Run the main application:

- **python main.py**


The agent will:

- Understand the user query

- Select the appropriate tool

- Execute the tool

- Return the final response

### 📌 Example Use Cases

- Solve mathematical calculations

- Find future dates

- Analyze text content

- Fetch real-time weather information

- Dynamically choose tools based on query intent

### 🧪 Learning Outcomes

- Practical understanding of LangChain Agents

- Tool invocation and orchestration

- Differences between single-tool and multi-tool agents

- External API integration with LLMs

- Clean and scalable project structuring for AI applications
