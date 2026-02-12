# Noor 🤍: Agentic AI Lifestyle Architect

**Noor** is a sophisticated, stateful multi-agent system designed to act as a 24/7 companion for mental health support and lifestyle architecture. Built using **LangGraph**, it leverages **Llama 3.3** to provide a seamless transition between emotional venting, disciplined habit tracking, and high-priority crisis intervention.

---

## 🏗️ Technical Architecture

### 1. Multi-Agent Orchestration
The core of Noor is a **Supervisor-Worker** pattern. Unlike linear chatbots, Noor uses a **StateGraph** to maintain context and route intent dynamically.



* **The Supervisor (The Brain):** Analyzes user messages using custom "Hyperbole Filters" to distinguish between casual stress (e.g., "This assignment is killing me") and actual crisis.
* **Specialized Expert Nodes:** * **Therapist Agent:** Employs Cognitive Behavioral Therapy (CBT) techniques to validate emotions and provide grounding exercises.
    * **Habit Agent:** A "Lifestyle Architect" focused on the **Core 4 Pillars**: Body, Mind, Soul, and Space. It utilizes the **2-Minute Rule** and **Identity Shifting** to drive action.
    * **Safety Agent:** A dedicated node for crisis intervention, assessing immediate risk and providing location-specific resources (India-based helplines like TeleMANAS).

### 2. State & Memory Persistence
Noor features **Long-Term Memory** via a `SqliteSaver` checkpointer. This allows the bot to:
* Maintain a thread-persistent `AgentState`.
* Store conversation history and user-specific data dynamically through a `user_name` field.
* Ensure persistence across system restarts by saving snapshots in a `memory.sqlite` database.

---

## 🧠 The "Core 4" Philosophy
Noor is programmed with a specific character grounded in discipline and integrity:
1.  **💪 Body:** Focuses on movement (10k steps), hydration, and rest.
2.  **🧠 Mind:** Prioritizes deep work, focus blocks, and continuous learning.
3.  **🧘‍♀️ Soul:** Rooted in grounding practices, gratitude, and prayer.
4.  **🏡 Space:** Emphasizes decluttering and managing digital peace.

---

## 🛠️ Tech Stack & Dependencies
* **LLM:** Llama-3.3-70b-versatile (via Groq API).
* **Framework:** LangGraph & LangChain (Stateful Orchestration).
* **Persistence:** SQLite (SqliteSaver).
* **Environment:** Python 3.12+.

---

## 🚀 Installation & Local Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Harneet9602/agentic-ai-chatbot.git](https://github.com/Harneet9602/agentic-ai-chatbot.git)
    cd agentic-ai-chatbot
    ```

2.  **Set up Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your Groq API Key:
    ```text
    GROQ_API_KEY=your_api_key_here
    ```

5.  **Run the Application:**
    ```bash
    python main.py
    ```

---
*"Discipline is the highest form of self-love." — Noor 🤍*
