"""
Customer Experience (CX) Impact and Trust Evaluation Module for SafeContext.

Evaluates user trust scores, friction points, and customer satisfaction feedback loops.
"""
from typing import Dict, Any, List

class CXTrustEvaluator:
    def __init__(self):
        self.feedback_log: List[Dict[str, Any]] = []

    def compute_trust_index(self, explanation_clarity: float, outcome_alignment: float) -> float:
        """Calculate composite customer trust index (0.0 - 1.0)."""
        return 0.5 * explanation_clarity + 0.5 * outcome_alignment

    def log_customer_feedback(self, interaction_id: str, rating: int, feedback: str) -> None:
        """Record customer feedback on AI explanations and system decisions."""
        self.feedback_log.append({
            "interaction_id": interaction_id,
            "rating": rating,
            "feedback": feedback
        })
