from typing import Tuple
def decide_policy(role_id: str) -> Tuple[str, str]:
    if role_id == "finance":
        return "gpt-4.1-mini", "finance-policy"
    if role_id == "health":
        return "gpt-4o", "health-policy"
    return "gpt-4o-mini", "default-policy"

