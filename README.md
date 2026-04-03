# 🤖 Multi-Agent AI Developer

A GenAI-powered system that simulates a real-world software engineering team using multiple AI agents for code generation, testing, and review.

---

## Live Demo

🔗 **(https://multi-agent-developer-hs2fszzhhexxrtt7b4ecpk.streamlit.app/)**  


---

## Overview

This project demonstrates a **multi-agent AI system** where different agents collaborate to solve coding tasks:

- **Developer Agent** – Generates clean and modular Python code  
- **Test Agent** – Creates unit tests and edge cases  
- **Reviewer Agent** – Improves code quality, fixes issues, and optimizes structure  

The system is powered by NVIDIA-hosted LLMs and includes a **premium interactive UI built with Streamlit**.

---

## Features

- Multi-agent collaboration (Dev + Test + Review)
- End-to-end AI coding pipeline
- Agentic workflow simulating real development lifecycle
- Premium Streamlit UI with live execution timeline
- Download generated code and test files
- Secure API handling using environment variables / secrets

---

## 🛠️ Tech Stack

- Python
- Streamlit
- NVIDIA LLM API (NIM)
- OpenAI-compatible SDK

---

## ⚙️ Setup Instructions

### **Clone the Repository**

git clone https://github.com/your-username/multi-agent-developer.git
cd multi-agent-developer

### **Install Dependencies**

```bash
pip install -r requirements.txt

### **Configure API Key**

For local setup, create a .env file:
```bash
API_KEY=your_api_key_here

For deployment (Streamlit Cloud), add the key in Secrets.

### **Run the App**
streamlit run ui.py

## Use Cases
###1. Rapid code prototyping
###2. Automated test generation
###3. Learning software development workflows
###4. Hackathon and demo projects
###5. AI-assisted development pipelines
