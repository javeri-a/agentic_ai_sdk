import streamlit as st
import asyncio
from agent_utils import run_agent

st.set_page_config(page_title="📚 Study Assistant", page_icon="📚")

st.title("📚 Study Assistant JavBOT")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_message(role, msg):
    st.session_state.history.append({"role": role, "msg": msg})

with st.form("study_form", clear_on_submit=True):
    question = st.text_input("Ask your study question")
    submitted = st.form_submit_button("Ask!")

if submitted and question.strip():
    add_message("user", question)

    with st.spinner("Typing..."):
        result = asyncio.run(run_agent(
            "You are a polite study assistant. Only answer study questions.",
            question
        ))
        add_message("bot", result)

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.info(msg["msg"])
    else:
        st.success(msg["msg"])
