# app.py
import streamlit as st
from multi_agent import run_education_system

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="EduAI - Multi Agent Learning System",
    page_icon="🎓",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------ #
st.markdown("""
<style>
.main {
    background-color: #f4f8fb;
}
.stTextInput>div>div>input {
    font-size: 18px;
}
.chat-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------ #
with st.sidebar:
    st.title("🎓 EduAI")
    st.markdown("### Multi-Agent Education System")
    st.markdown("---")
    difficulty = st.selectbox(
        "Select Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"]
    )
    st.markdown("---")
    st.info("Powered by CrewAI + Gemini")

# ------------------ HEADER ------------------ #
st.title("🎓 EduAI Learning Assistant")
st.markdown("Your AI Researcher + AI Writer working together to generate structured study notes.")

st.markdown("---")

# ------------------ SESSION STATE FOR CHAT ------------------ #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ USER INPUT ------------------ #
user_input = st.chat_input("Enter your study topic here...")

if user_input:

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("EduAI Agents are researching and writing..."):
            topic_with_level = f"{user_input} (Difficulty: {difficulty})"
            result = run_education_system(topic_with_level)

            st.markdown(result)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": result})

# ------------------ FOOTER ------------------ #
st.markdown("---")
st.caption("© 2026 EduAI | Multi-Agent Education System")
