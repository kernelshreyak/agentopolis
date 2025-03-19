import streamlit as st

from agentopolis_base.scenarios.sample_scenarios import escape_room_scenario
from agentopolis_base.agents.agents import initialize_agents, perform_scenario_response
from agentopolis_base.world.world_builder import initialize_world_resources
from agentopolis_base.data_models import SessionLocal,WorldActionModel

st.markdown("# Agentopolis - A sprawling city of agents")
st.markdown("### Agents")

st.markdown("### Choose from a scenario for the agents to respond to")
scenario_choice = st.selectbox("Choose Scenario",("Escape Room","Fire in a building"))
scenario = st.text_area("Scenario:",placeholder=escape_room_scenario,value=escape_room_scenario,height=150)

if st.button("Simulate"):
    st.success("Scenario submitted")

    scenario = escape_room_scenario

    st.info("Initializing world resources")
    world_resources = initialize_world_resources(scenario)
    # print("world_resources:",world_resources)
    st.markdown(f"""```json
    {world_resources}```""")

    st.info("Initializing agents")   
    agents_available = initialize_agents(world_resources)

    agents_selected = [agents_available['governor'], agents_available['banker'], agents_available['builder']]

    st.info("Performing scenario response")
    response = perform_scenario_response(scenario,world_resources,agents_available,agents_selected)

    st.markdown("### Scenario Response")
    st.markdown(f"""```json{response}```""")

