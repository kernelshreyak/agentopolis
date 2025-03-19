from agentopolis_base.world.world_prompt import agentopolis_world_prompt
from agentopolis_base.world.world_objects import WorldAction
from pydantic import BaseModel
from crewai import LLM
from dotenv import load_dotenv
import os
import json

load_dotenv()


class ResourceCreationWorldActions(BaseModel):
    resource_creations: list[WorldAction]

def initialize_world_resources(scenario: str):
    """The World-builder agent"""

    llm = LLM(model="gpt-4o",api_key=os.environ["OPENAI_API_KEY"],response_format=ResourceCreationWorldActions)

    worldbuilder_response = llm.call(f"""
            {agentopolis_world_prompt}
            Given the scenario in Agentopolis: {scenario}, create and initialize the resources needed by the agents to perform their tasks for this scenario. The resource creations are world actions in itself. And the output is an array of world actions specifying the resources created with their initial values and resource names. agent_slug for all the world actions is "worldbuilder". 
        """
    )
    worldbuilder_response = json.loads(worldbuilder_response)
    worldbuilder_response_txt = ""
    for resource_creation in worldbuilder_response['resource_creations']:
        worldbuilder_response_txt += "Resource Name: " + resource_creation['resource_name'] + ", Resource Value: " + str(resource_creation['resource_value']) + "\n"
    return worldbuilder_response_txt