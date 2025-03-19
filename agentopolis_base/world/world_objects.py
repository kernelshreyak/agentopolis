from pydantic import BaseModel
class WorldAction(BaseModel):
    resource_name: str
    agent_slug: str
    resource_value: int
    action: str