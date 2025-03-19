
from agentopolis_base.agents.agents_config import agents_dict
from crewai import Agent, Task, Crew
from typing import List
from agentopolis_base.data_models import SessionLocal,ScenarioResponseModel
from agentopolis_base.world.world_prompt import agentopolis_world_prompt

ENABLE_VERBOSE = True

def initialize_agents(world_resources: str):
    agents = dict()
    for agent_slug in agents_dict.keys():
        print(f"Initializing agent: {agent_slug}")
        agents[agent_slug] = Agent(
            role= agents_dict[agent_slug]["role"],
            goal=agents_dict[agent_slug]["goal"],
            backstory= f"""
            {agentopolis_world_prompt}
            Available world resources: {world_resources}
            {agents_dict[agent_slug]["backstory"]}
            """,
            verbose=ENABLE_VERBOSE,
            allow_delegation=agents_dict[agent_slug]["allow_delegation"],
            llm=agents_dict[agent_slug]["llm"],
            # max_tokens=100000
        )

    print("Agents initialized.")
    return agents


def perform_scenario_response(scenario:str,world_resources:str,intialized_agents: dict,selected_agents: List[Agent]):
    scenario_response_task = Task(
    description="""
        Given the scenario: {scenario}, perform a series of well defined world actions to resolve the scenario. The sequence of actions should make sense and the action attributes should be well defined and capture sufficient detail(the actions should not be simple phrases like "Unlock the fire extinguisher" but rather be more detailed like "unlock the fire extinguisher from the fire hydrant using the resource <resource_name> and using it to do <action>").
    """,
    expected_output="""
        A list of world actions(as JSON array, no other format) performed by the agents which defines the scenario response and achieves the scenario objectively.
    """,
    agent=intialized_agents['governor']
)
    agent_team =  Crew(
        agents=selected_agents,
        tasks=[scenario_response_task],
        verbose=ENABLE_VERBOSE
    )

    # db = SessionLocal()

    try:
        agent_slugs = ",".join(list(agents_dict.keys()))
        # datasource = db.query(DataSourceModel).filter(DataSourceModel.datasource_id == data_source_id).first()
        response = agent_team.kickoff(inputs={
            "scenario":scenario,
            "available_agent_slugs":agent_slugs,
            "agentopolis_world_prompt":agentopolis_world_prompt,
            "world_resources":world_resources,
            "available_agents":agent_slugs
        })
        # task.task_status = "completed"
        return response.raw
    except Exception as e:
        return "Task failed. Error: " + str(e)
    finally:
        # db.commit()
        pass


