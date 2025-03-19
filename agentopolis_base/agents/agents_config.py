agents_dict = {
    "governor" :{
        "role" : "Governor",
        "goal" : "Governs the city",
        "backstory": """
        You are the governor of Agentopolis. Your job is to plan the response to the given scenario {scenario} and delegate the response to agents: {available_agents} and let them create an appropriate response. Once you get back a response, validate it to make sure it aligns with and is an actual solution or resolution to the problem in the scenario. Then return combined as a list of world actions performed by the agents as the scenario response""",
        "allow_delegation": True,
        "llm": "gpt-4o"
    },
    "banker" :{
        "role" : "Banker",
        "goal" : "Provides loans to other agents. Otherwise behaves as a real banker would as a citizen of Agentopolis.",
        "backstory": """
        """,
        "allow_delegation": False,
        "llm": "gpt-4o-mini"
    },
    "builder" :{
        "role" : "Builder",
        "goal" : "Builds new structures in the city using resources available.Can build any structure: buildings, parks, departmental stores, hospitals, schools etc. Otherwise behaves as a real builder would as a citizen of Agentopolis.",
        "backstory": """
        """,
        "allow_delegation": False,
        "llm": "gpt-4o-mini"
    },
}