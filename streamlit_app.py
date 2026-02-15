import streamlit as st
from langchain_core.messages import HumanMessage
from graph import app
import uuid

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SEHAJ AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (THE PASTEL THEME) ---
st.markdown("""
    <style>
    /* MAIN BACKGROUND: Soft Cream */
    .stApp { background-color: #FFFDF5; }
    
    /* SIDEBAR: Soft Lavender */
    section[data-testid="stSidebar"] { background-color: #F3E5F5; border-right: 2px solid #E1BEE7; }
    
    /* CHAT BUBBLES */
    div[data-testid="stChatMessage"] {
        background-color: #F1F8E9;
        border: 1px solid #C5E1A5;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    
    /* USER BUBBLE COLOR */
    div[data-testid="stChatMessage"].st-emotion-cache-1c7y2kd {
        background-color: #E3F2FD;
        border: 1px solid #90CAF9;
    }
    
    /* HEADERS */
    h1, h2, h3 { color: #5D4037; font-family: 'Helvetica', sans-serif; }
    
    /* INFO BOX STYLING */
    div.stAlert { background-color: #FFF3E0; border: 1px solid #FFCCBC; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE SETUP ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a default welcome message
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "🌿 **Hello! I am Sehaj.** \n\nI am your Holistic AI Companion. I am here to balance your Mind, Body, and Soul. \n\nHow are you feeling right now?",
        "avatar": "🌿" # Default Avatar
    })

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_generic_persistent_session"

# --- 4. HELPER FUNCTION: DETECT AGENT AVATAR ---
def get_agent_style(content):
    """
    Scans the response text to guess which agent is speaking 
    and returns the appropriate avatar icon.
    """
    content_lower = content.lower()
    
    if "kai" in content_lower or "fitness" in content_lower or "rep" in content_lower or "gym" in content_lower:
        return "⚡" # Kai (Fitness)
    elif "serena" in content_lower or "therapist" in content_lower or "feel" in content_lower:
        return "🧘‍♀️" # Serena (Therapist)
    elif "noor" in content_lower or "habit" in content_lower or "core 4" in content_lower:
        return "🎋" # Noor (Habit - Bamboo)
    elif "turing" in content_lower or "professor" in content_lower or "research" in content_lower:
        return "🎓" # Turing (Professor)
    elif "pixel" in content_lower or "game" in content_lower or "trivia" in content_lower:
        return "👾" # Pixel (Games)
    elif "guardian" in content_lower or "helpline" in content_lower or "crisis" in content_lower:
        return "🛡️" # Guardian (Safety)
    else:
        return "🌿" # Default Sehaj

# --- 5. SIDEBAR (The Control Center) ---
with st.sidebar:
    st.markdown("## 🌿 **SEHAJ AI**")
    st.caption("Stateful Holistic AI Journal")
    st.markdown("---")
    
    st.subheader("⚙️ Preferences")
    user_name = st.text_input("What should I call you?", value="Friend")
    strict_mode = st.toggle("🔥 Beast Mode (Strict Coaching)", value=False)
    
    st.markdown("---")
    st.subheader("🤖 The Squad")
    
    with st.expander("🧘‍♀️ **Serena** (Therapist)", expanded=True):
        st.write("For emotions, venting, and CBT.")
    with st.expander("🎋 **Noor** (Habit Coach)"):
        st.write("For discipline and 'Core 4'.")
    with st.expander("⚡ **Kai** (Fitness)"):
        st.write("For gym splits and sleep data.")
    with st.expander("🎓 **Turing** (Professor)"):
        st.write("For study plans and research.")
    with st.expander("👾 **Pixel** (Games)"):
        st.write("For distraction and trivia.")
    with st.expander("🛡️ **Guardian** (Safety)"):
        st.write("Crisis intervention.")
        
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()

# --- 6. MAIN INTERFACE ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# 🌿") 
with col2:
    st.markdown("# Sehaj AI")
    st.markdown(f"*{user_name}'s Personal Sanctuary*")

# Static Examples
st.markdown("### 💡 Try Asking...")
e1, e2, e3, e4 = st.columns(4)
with e1: st.info("**💪 Fitness**\n\n'Give me a glute-focused gym plan.'")
with e2: st.info("**🥺 Support**\n\n'I feel overwhelmed and heavy today.'")
with e3: st.info("**📚 Study**\n\n'Find research papers on Deep Learning.'")
with e4: st.info("**🎲 Fun**\n\n'I am bored, let's play a game of Atlas!'")
st.markdown("---")

# --- 7. CHAT LOGIC ---

# Display History with Dynamic Avatars
for msg in st.session_state.messages:
    # Use the saved avatar if it exists, otherwise default to Sehaj leaf
    avatar_icon = msg.get("avatar", "🌿") if msg["role"] == "assistant" else None
    
    with st.chat_message(msg["role"], avatar=avatar_icon):
        st.markdown(msg["content"])

# Chat Input
user_input = st.chat_input("Type here... (e.g., 'I am procrastinating' or 'Help me sleep')")

if user_input:
    # 1. Display User Message immediately
    with st.chat_message("user"):
        st.markdown(user_input)
    # Save to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 2. Backend Processing
    with st.spinner("✨ Sehaj is thinking..."):
        try:
            # Config for persistence
            config = {"configurable": {"thread_id": st.session_state.thread_id}}
            
            # Prepare Input
            prompt_content = user_input
            if strict_mode:
                prompt_content += " (Note: The user wants TOUGH LOVE/STRICT mode)."

            input_state = {
                "messages": [HumanMessage(content=prompt_content)],
                "user_name": user_name
            }
            
            # CALL THE BRAIN (LangGraph)
            result = app.invoke(input_state, config=config)
            
            # Get Final Response
            bot_response = result['messages'][-1].content
            
            # DETECT AVATAR based on the response content
            detected_avatar = get_agent_style(bot_response)
            
            # 3. Display Assistant Response with NEW AVATAR
            with st.chat_message("assistant", avatar=detected_avatar):
                st.markdown(bot_response)
            
            # Save to history with the specific avatar
            st.session_state.messages.append({
                "role": "assistant", 
                "content": bot_response,
                "avatar": detected_avatar
            })
            
        except Exception as e:
            st.error(f"❌ Connection Error: {e}")
