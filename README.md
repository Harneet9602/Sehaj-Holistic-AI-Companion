# 🌿 SEHAJ AI: Stateful Holistic AI Journal

**SEHAJ** (Stateful Holistic AI Journal) is an agentic AI companion designed to balance **Mind, Body, and Soul**. Built on a multi-agent architecture using **LangGraph**, it autonomously routes user concerns to specialized AI experts—ranging from a CBT-based therapist to a technical research mentor.



---

## ✨ Key Features

* **🧠 Multi-Agent Orchestration:** Uses a "Supervisor" model to intelligently route queries to 6 specialized agents.
* **💾 Stateful Persistence:** Utilizes SQLite-based checkpointing to remember user history, preferences, and context across sessions.
* **🎨 Pastel UI:** A custom-styled Streamlit interface designed for a calming, non-clinical user experience with a "Soft UI" aesthetic.
* **🛡️ Safety First:** Integrated crisis detection with immediate redirection to emergency resources and Indian helplines (TeleMANAS, AASRA, etc.).

---

## 🤖 The Specialist Team (The Squad)

| Agent | Name | Specialty |
| :--- | :--- | :--- |
| **Therapist** | **Serena** | Emotional validation, CBT techniques, and stress management. |
| **Habit Coach** | **Noor** | Discipline, consistency, the "Core 4" pillars, and the 2-minute rule. |
| **Fitness** | **Kai** | Data-driven workout plans, sleep optimization, and diet strategy. |
| **Professor** | **Turing** | Academic support, DS/ML concept explanation, and research paper links. |
| **Distractor** | **Pixel** | Cognitive distraction through 14+ chat-based games (Atlas, Trivia, Riddles). |
| **Safety** | **Guardian** | Crisis intervention and emergency resource routing. |

---

## 🛠️ Technical Stack

* **LLM:** Llama-3.3-70b (via Groq API)
* **Framework:** [LangGraph](https://www.langchain.com/langgraph) (for agentic state management)
* **Interface:** [Streamlit](https://streamlit.io/)
* **Memory:** SQLite Checkpointer
* **Language:** Python 3.10+

---

## 🏗️ System Architecture

The system operates as a **Directed Acyclic Graph (DAG)**. 

1.  **Supervisor Node:** Analyzes user intent and selects the appropriate specialist.
2.  **Specialist Nodes:** Process the request based on their unique System Prompts and persona.
3.  **Checkpointer:** Every turn is saved in a SQLite database, allowing the bot to remember your name and past conversations even after the app restarts.



---

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AGENTIC-AI-CHATBOT.git](https://github.com/YOUR_USERNAME/AGENTIC-AI-CHATBOT.git)
    cd AGENTIC-AI-CHATBOT
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory:
    ```text
    GROQ_API_KEY=your_api_key_here
    ```

4.  **Run the application:**
    ```bash
    streamlit run streamlit_app.py
    ```

---

## 📝 License
Distributed under the MIT License.

---
*Created with 🤍 as a Data Science Capstone Project.*