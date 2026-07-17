class AmamiAgentAnalyticsClient:
    def evaluate_session(self, token_count: int, response_time_ms: int, user_satisfied: bool) -> dict:
        cost = round(token_count * 0.000002, 6)
        rating = "EXCELLENT" if user_satisfied and response_time_ms < 1500 else "NEEDS_OPTIMIZATION"
        return {"cost_usd": cost, "performance_rating": rating}