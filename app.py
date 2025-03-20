import streamlit as st

from agentopolis_base.scenarios.sample_scenarios import get_scenarios
from agentopolis_base.agents.agents import initialize_agents, perform_scenario_response
from agentopolis_base.world.world_builder import initialize_world_resources,transform_scenario_response
from agentopolis_base.data_models import SessionLocal,WorldActionModel,WorldModel,ScenarioResponseModel
from agentopolis_base.agents.agents_config import agents_dict
import json

def create_world():
    db = SessionLocal()
    try:
        # check if a world already exists
        world = db.query(WorldModel).first()
        if world:
            st.info("World already exists: " + world.name)
            return world
        st.info("Creating default world")
        world = WorldModel(**{
            "name":"Agentopolis Default World"
        })
        db.add(world)
        db.commit()
        db.refresh(world)
        st.success("World created")
        return world
    finally:
        db.close()

current_world = create_world()

st.markdown("# Agentopolis - A City of Agents")
st.markdown("A sprawling city of agents with a common goal.")
st.markdown("### Agents (choose at least one)")
chosen_agents = dict()
for agent in agents_dict.keys():
    if agent == 'governor':
        continue
    chosen_agents[agent] = st.checkbox(f"{agents_dict[agent]['role']}", key=agent)


st.markdown("### Choose from a scenario for the agents to respond to")
available_scenarios = get_scenarios() 
scenario_choice = st.selectbox("Choose Scenario",tuple(available_scenarios.keys()))
chosen_scenario = available_scenarios[scenario_choice]
st.markdown("Scenario sample (copy it to next text area):")
st.markdown(f"""```{chosen_scenario}```""")
scenario = st.text_area("Scenario:",placeholder="Describe the scenario",height=150)
if st.button("Simulate"):
    if scenario == "":
        st.error("Scenario cannot be empty")
        st.stop()
    st.success("Scenario submitted")
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
    if len(agents_selected) == 0:
        st.error("No agents selected. Cannot proceed")
        st.stop()
    st.info("Performing scenario response")
    response = perform_scenario_response(scenario,world_resources,agents_available,agents_selected)
     # mock response
    # response = """{"world_actions": [{"action": "move", "agent_slug": "builder", "target": "fire hydrant", "resource": "fire extinguisher", "resource_name": "fire extinguisher","simulated_time_taken":"10s"}, {"action": "unlock", "agent_slug": "builder", "target": "fire hydrant", "resource": "fire extinguisher", "resource_name": "fire extinguisher","simulated_time_taken": "10s"}] }"""
    
    scenario_response_json = transform_scenario_response(response)
    type(scenario_response_json)
    print("scenario_response_json",scenario_response_json)
    st.markdown("### Scenario Response")
    st.markdown(f"""```json{response}```""")

    # persist world actions
    st.info("Saving scenario response and world actions")
    db = SessionLocal()
    scenario_response = ScenarioResponseModel(**{
        "scenario_response_report":response,
        "world_id":current_world.world_id,
    })
    db.add(scenario_response)
    db.commit()

    for action in scenario_response_json['world_actions']:
        world_action = WorldActionModel(**action)
        world_action.scenario_response_id = scenario_response.scenario_response_id
        db.add(world_action)
    db.commit()
    db.close()

