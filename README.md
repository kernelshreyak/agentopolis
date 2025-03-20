# Agentopolis - A Sprawling City of Agents

Agentopolis is an open source project that enables simulation of complex scenarios with agents.

The project defines a city called Agentopolis with a set of agents that can interact with each other and the world. The world is made up of resources and the agents can perform actions on the resources to change the world state.

The project allows users to create scenarios and define the agents' goals and backstories. The agents can then be run in a simulation and the results can be viewed in a reporting dashboard.

The project is built using Python and the following frameworks:

* Streamlit for the reporting dashboard
* SQLAlchemy for the database
* Pydantic for data models
* CrewAI for agent management


The project uses the following components:

* **CrewAI**: An open source framework for building and managing agents. It provides a simple way to create agents and define their roles, goals, backstories, and behaviors.
* **Streamlit**: A Python library for creating web applications. It is used to create the reporting dashboard where scenarios can be created and run.
* **SQLAlchemy**: A Python library for interacting with databases. It is used to create the database schema and interact with the database.
* **Pydantic**: A Python library for creating data models. It is used to define the data models for the agents and the world.

The project is organized into the following directories:

* **agentopolis_base**: This directory contains the base code for the project including the agents, the world, and the data models.



* **scenarios**: This directory contains the scenarios that can be run. Each scenario is a separate directory and contains a description of the scenario, the agents' goals and backstories, and the resources and agents available in the scenario.
* **world**: This directory contains the code for the world including the resources and the rules of the world. The resources are defined in the `world/resources` directory and the rules of the world are defined in the `world/rules` directory.
* **agents**: This directory contains the code for the agents including their roles, goals, backstories, and behaviors. The agents are defined in the `agents/agents` directory.
