escape_room_scenario = """
There is an small, dimly-lit room with following resources in it: 1 x Rope, 2 x steel rod, 5 x bottle.
The overall objective is for all people to escape the room using any of the available resources/items.
"""

fire_in_a_building_scenario = """
There is a fire in a building.
The overall objective is for all people to escape the building using any of the available resources/items and also help in extinguishing the fire. Building has these resources: 10 x Bucket,1 x water tap, 2 x fire extinguisher(but locked), 3 x ropes
"""


def get_scenarios():
    return {
        "Escape Room": escape_room_scenario,
        "Fire in a building": fire_in_a_building_scenario
    }