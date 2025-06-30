import streamlit as st
import asyncio
from agent_utils import run_agent

st.set_page_config(page_title="💪 Fitness Coach", page_icon="💪")

st.title("💪 Fitness Coach")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_message(role, msg):
    st.session_state.history.append({"role": role, "msg": msg})

with st.form("fitness_form", clear_on_submit=True):
    age = st.number_input("Age", 10, 100, 25)
    fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.selectbox("Goal", ["Muscle Gain", "Fat Loss", "Endurance"])
    submitted = st.form_submit_button("Get Workout Plan!")

if submitted:
    prompt = f"""
    I am {age} years old, my fitness level is {fitness_level}, goal is {goal}.
    Suggest a weekly workout plan and 3 fitness tips in simple Urdu-English.
    """
    add_message("user", prompt)

    with st.spinner("Preparing your plan..."):
        result = asyncio.run(run_agent(
            "You are a helpful fitness coach. Provide friendly workout plans and health tips.",
            prompt
        ))
        add_message("bot", result)

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.info(msg["msg"])
    else:
        st.success(msg["msg"])
