import os
import json

# Disable CrewAI telemetry by default to avoid Streamlit thread signal issues.
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")
os.environ.setdefault("OTEL_SDK_DISABLED", "true")

from agentopolis_base.world.world_prompt import agentopolis_world_prompt
from agentopolis_base.world.world_objects import WorldAction
from pydantic import BaseModel
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()


class ResourceCreationWorldActions(BaseModel):
    resource_creations: list[WorldAction]

class WorldActions(BaseModel):
    world_actions: list[WorldAction]

def initialize_world_resources(scenario: str):
    """The World-builder agent"""

    llm = LLM(model="gpt-4o",api_key=os.environ["OPENAI_API_KEY"],response_format=ResourceCreationWorldActions)
    worldbuilder_response = llm.call(f"""
            {agentopolis_world_prompt}
            Given the scenario in Agentopolis: {scenario}, create and initialize the resources needed by the agents to perform their tasks for this scenario. The resource creations are world actions in itself. And the output is an array of world actions specifying the resources created with their initial values and resource names. agent_slug for all the world actions is "worldbuilder". 
            Do not create any resources which were not part of the scenario in its definition.
        """
    )
    if isinstance(worldbuilder_response, str):
        worldbuilder_response = json.loads(worldbuilder_response)
    elif hasattr(worldbuilder_response, "model_dump"):
        worldbuilder_response = worldbuilder_response.model_dump()
    worldbuilder_response_txt = ""
    for resource_creation in worldbuilder_response['resource_creations']:
        worldbuilder_response_txt += "Resource Name: " + resource_creation['resource_name'] + ", Resource Value: " + str(resource_creation['resource_value']) + "\n"
    return worldbuilder_response_txt

def transform_scenario_response(scenario_response: str) -> list[WorldAction]:
    llm = LLM(model="gpt-4o-mini",api_key=os.environ["OPENAI_API_KEY"],response_format=WorldActions)
    transformed_response = llm.call(f"""
            Given this output from the scenario response agent: {scenario_response} which contains a JSON portion with a list of world actions, transform it into a list of world actions as per response format. retaining all the information and ignoring any non-JSON text". 
        """
    )
    if isinstance(transformed_response, str):
        transformed_response = json.loads(transformed_response)
    elif hasattr(transformed_response, "model_dump"):
        transformed_response = transformed_response.model_dump()
    return transformed_response
