from app.models import Reward

def compute_reward(task, action, step):

    obs = task["observation"]
    expected = task["expected"]

    score = 0.0

    # ✅ correct
    if action.decision == expected:
        score = 1.0

    # ⚠️ partial
    elif action.decision == "request_verification":
        score = 0.5

    # 🚨 fraud penalty
    if obs.previous_claims > 3 and obs.last_claim_days_ago < 30:
        if action.decision != "flag_for_audit":
            score -= 0.7

    # ⏱️ step penalty
    score -= 0.05 * step

    score = max(0.0, min(1.0, score))

    return Reward(
        score=score,
        feedback=f"{expected} vs {action.decision} | reason: {action.reason}"
    )