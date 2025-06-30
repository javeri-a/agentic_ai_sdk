import streamlit as st
import asyncio
from agent_utils import run_agent

st.set_page_config(page_title="🥗 Meal Mentor", page_icon="🥗")

st.title("🥗 Meal Mentor — Your Healthy Food Guide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_message(role, msg):
    st.session_state.history.append({"role": role, "msg": msg})

with st.form("meal_form", clear_on_submit=True):
    age = st.number_input("Age", 10, 100, 25)
    weight = st.number_input("Weight (kg)", 30, 200, 60)
    goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Maintenance"])
    pref = st.text_input("Food Preferences", "Vegetarian")
    submitted = st.form_submit_button("Get Plan!")

if submitted:
    prompt = f"""
    I am {age} years old, weigh {weight} kg.
    My goal is {goal}.
    I prefer: {pref}.
    Create breakfast, lunch, dinner, snacks + 3 health tips in simple Urdu-English.
    """
    add_message("user", prompt)

    with st.spinner("Thinking..."):
        result = asyncio.run(run_agent(
            "You are a polite meal mentor who only helps with healthy food advice.",
            prompt
        ))
        add_message("bot", result)

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.info(msg["msg"])
    else:
        st.success(msg["msg"])
