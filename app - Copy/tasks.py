import random
from app.models import Observation

def get_task():
    return random.choice([
        easy_task(),
        medium_task(),
        hard_task()
    ])

def easy_task():
    return {
        "id": "easy",
        "expected": "approve",
        "observation": Observation(
            income_level="low",
            family_size=4,
            documents_verified=True,
            previous_claims=1,
            region_type="rural",
            last_claim_days_ago=120
        )
    }

def medium_task():
    return {
        "id": "medium",
        "expected": "request_verification",
        "observation": Observation(
            income_level="medium",
            family_size=3,
            documents_verified=False,
            previous_claims=2,
            region_type="urban",
            last_claim_days_ago=40
        )
    }

def hard_task():
    return {
        "id": "hard",
        "expected": "flag_for_audit",
        "observation": Observation(
            income_level="low",
            family_size=5,
            documents_verified=True,
            previous_claims=5,
            region_type="urban",
            last_claim_days_ago=5
        )
    }