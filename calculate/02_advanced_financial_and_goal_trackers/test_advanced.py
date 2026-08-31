"""
Unit Test Suite for Advanced Financial & Goal Trackers Module.

Tests CreditCardRepaymentCalculator, WeightLossGoalTracker, and GoalGrowthTracker classes.
"""

import datetime
import unittest
from financial_and_goal_trackers import (
    CreditCardRepaymentCalculator,
    GoalGrowthTracker,
    WeightLossGoalTracker,
)


class TestFinancialAndGoalTrackers(unittest.TestCase):
    """Test cases for credit repayment, weight loss, and growth calculation models."""

    def test_credit_card_repayment_schedule(self) -> None:
        """Verify credit card repayment schedule calculation and balance zeroing."""
        calc = CreditCardRepaymentCalculator(
            initial_balance=1000.0, annual_interest_rate=0.12, monthly_payment=200.0
        )
        schedule, total_interest = calc.calculate_repayment_schedule(
            datetime.date(2026, 1, 1)
        )
        self.assertGreater(len(schedule), 0)
        self.assertEqual(schedule[-1]["remaining_balance"], 0.0)
        self.assertGreater(total_interest, 0.0)

    def test_credit_card_repayment_insufficient_payment(self) -> None:
        """Verify OverflowError when monthly payment is smaller than monthly interest charge."""
        calc = CreditCardRepaymentCalculator(
            initial_balance=10000.0, annual_interest_rate=0.50, monthly_payment=10.0
        )
        with self.assertRaises(OverflowError):
            calc.calculate_repayment_schedule(datetime.date(2026, 1, 1))

    def test_weight_loss_goal_tracker(self) -> None:
        """Verify weight loss completion date calculation."""
        tracker = WeightLossGoalTracker(
            current_weight=100.0, target_weight=80.0, avg_loss_per_week=1.0
        )
        start_date = datetime.date(2026, 1, 1)
        target_date, weeks = tracker.estimate_completion_date(start_date)

        self.assertEqual(weeks, 20)  # 20 kg / 1 kg/week = 20 weeks
        self.assertEqual(target_date, start_date + datetime.timedelta(days=140))

    def test_goal_growth_tracker(self) -> None:
        """Verify subscriber goal growth calculation days."""
        days = GoalGrowthTracker.estimate_days_to_target(
            current_metric=65000, target_metric=100000, avg_per_day=700.0
        )
        self.assertEqual(days, 50)  # 35000 / 700 = 50 days

        # Metric already achieved case
        self.assertEqual(
            GoalGrowthTracker.estimate_days_to_target(100, 50, 10.0), 0
        )


if __name__ == "__main__":
    unittest.main()
