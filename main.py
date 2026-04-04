from fastapi import FastAPI
from pydantic import BaseModel
from inference import run

app = FastAPI()

# -------------------------------
# Request model for /step
# -------------------------------
class ActionRequest(BaseModel):
    action: str


# -------------------------------
# Home route
# -------------------------------
@app.get("/")
def home():
    return {"message": "Global Welfare Env Running"}


# -------------------------------
# OpenEnv REQUIRED: RESET
# -------------------------------
@app.post("/reset")
def reset():
    return {
        "observation": {
            "income_level": "low",
            "family_size": 4,
            "documents_verified": True,
            "previous_claims": 1,
            "region_type": "rural",
            "last_claim_days_ago": 60
        },
        "reward": 0.0,
        "done": False,
        "info": {}
    }


# -------------------------------
# OpenEnv REQUIRED: STEP
# -------------------------------
@app.post("/step")
def step(request: ActionRequest):
    action = request.action

    # simple logic (you can improve later)
    if action == "approve":
        reward = 1.0
        done = True
    elif action == "reject":
        reward = 0.8
        done = True
    elif action == "flag_for_audit":
        reward = 0.95
        done = True
    elif action == "request_verification":
        reward = 0.5
        done = False
    else:
        reward = -1.0
        done = True

    return {
        "observation": {
            "status": "processed",
            "action_taken": action
        },
        "reward": reward,
        "done": done,
        "info": {}
    }


# -------------------------------
# Optional: run full inference
# -------------------------------
@app.get("/run")
def run_env():
    run()
    return {"status": "executed"}
