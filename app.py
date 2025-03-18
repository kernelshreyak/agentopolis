import streamlit as st

from agentopolis_base.prompts.sample_scenarios import escape_room_scenario

st.markdown("# Agentopolis - A sprawling city of agents")
st.markdown("### Agents")

st.markdown("### Choose from a scenario for the agents to respond to")
scenario_choice = st.selectbox("Choose Scenario",("Escape Room","Fire in a building"))
st.text_area("Scenario:",placeholder=escape_room_scenario)
