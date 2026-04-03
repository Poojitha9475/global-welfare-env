from pydantic import BaseModel

class Observation(BaseModel):
    income_level: str
    family_size: int
    documents_verified: bool
    previous_claims: int
    region_type: str
    last_claim_days_ago: int

class Action(BaseModel):
    decision: str
    reason: str   

class Reward(BaseModel):
    score: float
    feedback: str