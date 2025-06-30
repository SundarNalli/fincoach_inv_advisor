from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    income: float
    goal: str
    children: int = 0
    risk_tolerance: str | None = None
    response_content: str
    advice: str