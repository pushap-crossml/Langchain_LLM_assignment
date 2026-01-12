# LangChain Agent with Persistent Memory (Mem0) and Tooling

An **industry-grade LangChain application** demonstrating how to build a **tool-augmented AI agent** with **persistent long-term memory**, **external API integrations**, and **production-ready logging**.

---

## 📌 Overview

This project showcases best practices for building robust LLM-powered systems, including:

- Stateless agent execution with stateful behavior via external memory  
- Secure credential management  
- Modular, tool-driven agent design  
- Enterprise-grade logging and error handling  
- Interactive and scripted execution modes  

---

## 🚀 Key Features

### 🧠 Persistent Memory (Mem0)
- Long-term memory across conversations  
- Semantic memory retrieval based on user queries  
- Graceful fallback when memory is unavailable  
- Memory injected directly into the system prompt  

### 🤖 Tool-Driven Agent Intelligence
The agent automatically selects and invokes tools for:

- Safe arithmetic evaluation  
- Date calculations  
- Text analysis (statistics + sentiment)  
- Live weather data with practical recommendations  

### 🔐 Secure Credential Management
- API keys loaded from environment variables or `.env`  
- Required credentials validated at startup  
- Optional dependencies fail gracefully  
- No secrets hard-coded in source  

### 📜 Enterprise-Grade Logging
- Rotating log files with retention  
- Console and file-based logging  
- Structured, readable log format  
- Debug-friendly traceability  

### 💬 Multiple Execution Modes
- Interactive REPL-style chat  
- Predefined example queries for testing and demos  

---

## 🛠️ Technology Stack

- **Python** 3.10+  
- **LangChain**  
- **Google Gemini** (`langchain-google-genai`)  
- **Mem0** (Persistent Memory Store)  
- **OpenWeatherMap API**  
- **python-dotenv**  
- **AST-based safe expression evaluation**  

---

## 📦 Dependencies

```txt
langchain==1.2.0
langchain-google-genai==4.1.2
mem0ai==1.0.1
python-dotenv==1.2.1

## Environment Variables

Create a `.env` file (**never commit it**) with the following variables:

```env
GEMINI_API_KEY=your_google_gemini_api_key
WEATHER_API_KEY=your_openweathermap_api_key
MEM0_API_KEY=your_mem0_api_key
GEMINI_API_KEY – Required for LLM access

WEATHER_API_KEY – Required for weather tool functionality

MEM0_API_KEY – Optional; enables persistent memory
