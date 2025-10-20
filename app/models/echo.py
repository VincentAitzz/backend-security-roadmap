from pydantic import BaseModel, Field

class EchoRequest(BaseModel):
    name: str = Field(...,min_length=1,max_length=50)
    age: int = Field(...,ge=0,le=150)