from pydantic import BaseModel

class GenerateRequest(BaseModel):
    event: str
    interest: str