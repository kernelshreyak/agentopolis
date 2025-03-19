# testing a simulation run for Agentopolis

from agentopolis_base.scenarios.sample_scenarios import escape_room_scenario
from agentopolis_base.agents.agents import initialize_agents, perform_scenario_response
from agentopolis_base.world.world_builder import initialize_world_resources

scenario = escape_room_scenario

world_resources = initialize_world_resources(scenario)
print("world_resources:",world_resources)

agents_available = initialize_agents(world_resources)

agents_selected = [agents_available['governor'], agents_available['banker'], agents_available['builder']]

response = perform_scenario_response(scenario,world_resources,agents_available,agents_selected)
print(response)