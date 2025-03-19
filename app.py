import streamlit as st

from agentopolis_base.scenarios.sample_scenarios import get_scenarios
from agentopolis_base.agents.agents import initialize_agents, perform_scenario_response
from agentopolis_base.world.world_builder import initialize_world_resources
from agentopolis_base.data_models import SessionLocal,WorldActionModel
from agentopolis_base.agents.agents_config import agents_dict

st.markdown("# Agentopolis - A sprawling city of agents")
st.markdown("### Agents (choose at least one")
chosen_agents = dict()
for agent in agents_dict.keys():
    if agent == 'governor':
        continue
    chosen_agents[agent] = st.checkbox(f"{agents_dict[agent]['role']}", key=agent)


st.markdown("### Choose from a scenario for the agents to respond to")
available_scenarios = get_scenarios()
scenario_choice = st.selectbox("Choose Scenario",tuple(available_scenarios.keys()))
chosen_scenario = available_scenarios[scenario_choice]
scenario = st.text_area("Scenario:",placeholder="Describe the scenario",value=chosen_scenario,height=150)

if st.button("Simulate"):
    st.success("Scenario submitted")

    scenario = chosen_scenario

    st.info("Initializing world resources")
    world_resources = initialize_world_resources(scenario)
    # print("world_resources:",world_resources)
    st.markdown(f"""```json
    {world_resources}```""")

    st.info("Initializing agents")   
    agents_available = initialize_agents(world_resources)

    agents_selected = []
    for agent in chosen_agents.keys():
        if chosen_agents[agent]:
            agents_selected.append(agents_available[agent])
    st.write([agent.role for agent in agents_selected])
    st.info("Performing scenario response")
    response = perform_scenario_response(scenario,world_resources,agents_available,agents_selected)

    st.markdown("### Scenario Response")
    st.markdown(f"""```json{response}```""")

