escape_room_scenario = """
There is an small, dimly-lit room with following resources in it: 1 x Rope, 2 x steel rod, 5 x bottle.
The overall objective is for all people to escape the room using any of the available resources/items.
"""

fire_in_a_building_scenario = """
There is a fire in a building.
The overall objective is for all people to escape the building using any of the available resources/items and also help in extinguishing the fire. Building has these resources: 10 x Bucket,1 x water tap, 2 x fire extinguisher(but locked), 3 x ropes
"""

box_opening_competition_scenario = """
There is 1 x iron box (one for each agent). The overall objective is for the agents to compete with each other to open the boxes in the shortest possible time using available resources.
Available resources: 1 x iron box(which needs to be opened), 4 x pencils, 1 x gas stove, 1 x metal sheet, 1 x bucket of water
"""

def get_scenarios():
    return {
        "Escape Room": escape_room_scenario,
        "Fire in a building": fire_in_a_building_scenario,
        "Box opening competition": box_opening_competition_scenario
    }