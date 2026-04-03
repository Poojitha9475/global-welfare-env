import os
from openai import OpenAI
from app.env import WelfareEnv
from app.models import Action


# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# OPENAI CLIENT

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


# DECISION FUNCTION (MULTI-STEP + EXPLAINABLE)
def get_action(obs, step):

    # STEP 1 → check missing docs
    if step == 1 and not obs.documents_verified:
        return {
            "decision": "request_verification",
            "reason": "documents are missing"
        }

    # FRAUD DETECTION (time-based)
    if obs.previous_claims > 3 and obs.last_claim_days_ago < 30:
        return {
            "decision": "flag_for_audit",
            "reason": "too many recent claims"
        }

    # HIGH INCOME → reject
    if obs.income_level == "high":
        return {
            "decision": "reject",
            "reason": "income too high"
        }

    # LOW INCOME → approve
    if obs.income_level == "low" and obs.documents_verified:
        return {
            "decision": "approve",
            "reason": "eligible low income"
        }

    # DEFAULT
    return {
        "decision": "request_verification",
        "reason": "insufficient information"
    }

# MAIN RUN
def run():
    env = WelfareEnv()
    obs = env.reset()

    step = 0
    rewards = []
    success = False

    print(f"[START] task=welfare env=openenv model={MODEL_NAME}")

    try:
        while True:
            step += 1

            decision_data = get_action(obs, step)

            action = Action(
                decision=decision_data["decision"],
                reason=decision_data["reason"]
            )

            obs, reward, done, _ = env.step(action)

            rewards.append(round(reward.score, 2))

            print(
                f"[STEP] step={step} action={decision_data['decision']} "
                f"reward={reward.score:.2f} done={str(done).lower()} error=null"
            )

            if done:
                success = reward.score > 0.8
                break

    except Exception as e:
        print(
            f"[STEP] step={step} action=error reward=0.00 done=true error={str(e)}"
        )

    print(
        f"[END] success={str(success).lower()} steps={step} "
        f"rewards={','.join([f'{r:.2f}' for r in rewards])}"
    )

# ENTRY POINT
if __name__ == "__main__":
    run()