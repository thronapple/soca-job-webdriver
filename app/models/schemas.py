from pydantic import BaseModel

class Action(BaseModel):
    action_type: str
    parameters: dict
