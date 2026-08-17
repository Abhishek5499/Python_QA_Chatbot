import streamlit as st

from chatbot import get_answer


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Python Q&A Chatbot",
    page_icon="🐍",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("🐍 Personal Python Q&A Chatbot")

st.write(
    "Ask questions about Python programming "
    "and get answers from the Python knowledge base."
)


# ==========================================
# INFORMATION
# ==========================================

st.info(
    "You can ask questions about Python basics, "
    "variables, data types, loops, functions, "
    "OOP, NumPy, Pandas, and more."
)


# ==========================================
# USER INPUT
# ==========================================

user_question = st.text_input(
    "Enter your Python question:",
    placeholder="Example: What is a list in Python?"
)


# ==========================================
# ASK BUTTON
# ==========================================

if st.button("Ask Chatbot"):

    if user_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        answer = get_answer(user_question)

        st.subheader("🤖 Chatbot Answer")

        st.success(answer)


# ==========================================
# EXAMPLE QUESTIONS
# ==========================================

st.divider()

st.subheader("Example Questions")

st.write("• What is Python?")
st.write("• What is a list?")
st.write("• What is a tuple?")
st.write("• What is a function?")
st.write("• What is a for loop?")
st.write("• What is inheritance?")
st.write("• What is NumPy?")
st.write("• What is Pandas?")