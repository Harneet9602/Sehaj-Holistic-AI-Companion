import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import (
    supervisor_node,
    therapist_node,
    habit_node,
    fitness_node,
    professor_node,
    games_node,
    safety_node
)

# 1. Setup the Database Connection (The Memory Bank)
# check_same_thread=False is needed for Streamlit to not crash
conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
memory = SqliteSaver(conn)

# 2. Initialize the Graph
workflow = StateGraph(AgentState)

# 3. Register the Nodes
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("therapist", therapist_node)
workflow.add_node("habit", habit_node)
workflow.add_node("fitness", fitness_node)
workflow.add_node("professor", professor_node)
workflow.add_node("games", games_node)
workflow.add_node("safety", safety_node)

# 4. Set Entry Point
workflow.set_entry_point("supervisor")

# 5. Add Routing Logic
workflow.add_conditional_edges(
    "supervisor",
    lambda state: state['next'],
    {
        "THERAPIST": "therapist",
        "HABIT": "habit",
        "FITNESS": "fitness",
        "PROFESSOR": "professor",
        "GAMES": "games",
        "SAFETY": "safety"
    }
)

# 6. Returns
workflow.add_edge("therapist", END)
workflow.add_edge("habit", END)
workflow.add_edge("fitness", END)
workflow.add_edge("professor", END)
workflow.add_edge("games", END)
workflow.add_edge("safety", END)

# 7. Compile with Memory (CRITICAL STEP)
# This enables the bot to "remember" past turns
app = workflow.compile(checkpointer=memory)