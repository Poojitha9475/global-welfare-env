# 🌍 Global Benefit Eligibility & Fraud Detection OpenEnv

##  Overview
This project implements an OpenEnv reinforcement learning environment where an AI agent learns to evaluate eligibility for social benefit programs and detect fraudulent claims.

The system simulates real-world decision-making used in government welfare systems globally.

---

##  Key Features

- ✅ Multi-step decision workflow
- ✅ Explainable AI (decision reasoning)
- ✅ Time-based fraud detection
- ✅ Reward shaping with penalties
- ✅ Hybrid decision system (rule-based + LLM-ready)
- ✅ Real-world inspired environment

---

##  Problem Statement

Governments worldwide face challenges in:
- Incorrect benefit approvals
- Fraudulent repeated claims
- Inefficient verification workflows

This environment enables AI agents to learn optimal decision-making policies to address these issues.

---

## ⚙️ Environment Design

### Observation Space
- income_level
- family_size
- documents_verified
- previous_claims
- region_type
- last_claim_days_ago

---

### Action Space
- approve
- reject
- request_verification
- flag_for_audit

---

##  Reward System

- Correct decision → +1.0  
- Partial decision → +0.5  
- Fraud missed → penalty  
- Step cost penalty → -0.05 per step  

---

## Multi-Step Workflow

1. Request verification (if needed)
2. Final decision (approve/reject/audit)

---

## Example Output
[START] task=welfare env=openenv model=gpt-4.1-mini
[STEP] step=1 action=request_verification reward=0.45 done=false error=null
[STEP] step=2 action=approve reward=0.95 done=true error=null
[END] success=true steps=2 rewards=0.45,0.95
---

## Why This Matters

-  Globally applicable welfare system
-  Fraud detection using behavioral patterns
-  Real-world decision modeling
-  AI-ready environment for RL training

---

## Future Improvements

- Identity fraud detection
- Cross-region duplicate claims
- LLM-based reasoning
- Dynamic policy learning

---

## 👨‍💻 Author
