"""
Advanced Financial Repayment & Goal Projection Calculators Module.

This module implements object-oriented financial repayment and goal tracking algorithms:
- `CreditCardRepaymentCalculator`: Amortization calculator with monthly interest compounding
- `WeightLossGoalTracker`: Target weight reduction schedule and completion date calculator
- `GoalGrowthTracker`: Proportional growth projection calculator (e.g. subscribers/followers)

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

import calendar
import datetime
import math
from typing import Any, Dict, List, Tuple


class CreditCardRepaymentCalculator:
    """
    Credit card monthly payment amortization schedule calculator.
    """

    def __init__(self, initial_balance: float, annual_interest_rate: float, monthly_payment: float) -> None:
        """
        Initializes repayment calculator parameters.

        Args:
            initial_balance (float): Total starting credit balance.
            annual_interest_rate (float): Annual interest percentage rate (e.g. 0.26 for 26%).
            monthly_payment (float): Fixed monthly payment amount.
        """
        if initial_balance <= 0 or monthly_payment <= 0:
            raise ValueError("Balance and monthly payment must be positive numbers.")

        self.initial_balance = initial_balance
        self.annual_interest_rate = annual_interest_rate
        self.monthly_payment = monthly_payment

    def calculate_repayment_schedule(
        self, start_date: datetime.date
    ) -> Tuple[List[Dict[str, Any]], float]:
        """
        Calculates month-by-month repayment schedule and total interest accumulated.

        Args:
            start_date (datetime.date): Initial repayment starting date.

        Returns:
            Tuple[List[Dict[str, Any]], float]: Schedule breakdown list and total interest paid.
        """
        current_balance = self.initial_balance
        current_date = start_date
        schedule: List[Dict[str, Any]] = []
        total_interest_paid = 0.0

        monthly_rate = self.annual_interest_rate / 12.0

        while current_balance > 0:
            interest_charge = round(current_balance * monthly_rate, 2)
            total_interest_paid += interest_charge
            current_balance += interest_charge

            payment = min(current_balance, self.monthly_payment)
            current_balance = round(current_balance - payment, 2)

            # Advance to next month date
            days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
            current_date += datetime.timedelta(days=days_in_month)

            schedule.append({
                "payment_date": current_date.isoformat(),
                "interest_charge": interest_charge,
                "payment_made": payment,
                "remaining_balance": current_balance,
            })

            if len(schedule) > 600:  # Prevent infinite loop if interest > payment
                raise OverflowError("Monthly payment is insufficient to cover interest charges.")

        return schedule, round(total_interest_paid, 2)


class WeightLossGoalTracker:
    """
    Weekly weight loss milestone and completion date calculator.
    """

    def __init__(self, current_weight: float, target_weight: float, avg_loss_per_week: float) -> None:
        """
        Initializes weight loss parameters.

        Args:
            current_weight (float): Starting weight in kg/lbs.
            target_weight (float): Goal target weight in kg/lbs.
            avg_loss_per_week (float): Average expected loss per week.
        """
        if current_weight <= target_weight or avg_loss_per_week <= 0:
            raise ValueError("Current weight must exceed target weight, and weekly loss must be > 0.")

        self.current_weight = current_weight
        self.target_weight = target_weight
        self.avg_loss_per_week = avg_loss_per_week

    def estimate_completion_date(self, start_date: datetime.date) -> Tuple[datetime.date, int]:
        """
        Calculates target completion date and total weeks needed.

        Args:
            start_date (datetime.date): Starting date.

        Returns:
            Tuple[datetime.date, int]: Estimated completion date and total weeks.
        """
        weight_to_lose = self.current_weight - self.target_weight
        total_weeks = math.ceil(weight_to_lose / self.avg_loss_per_week)
        target_date = start_date + datetime.timedelta(days=total_weeks * 7)
        return target_date, total_weeks


class GoalGrowthTracker:
    """
    Target metric growth projection calculator (e.g. YouTube subscribers).
    """

    @staticmethod
    def estimate_days_to_target(
        current_metric: int, target_metric: int, avg_per_day: float
    ) -> int:
        """
        Calculates estimated days to reach target growth metric.

        Args:
            current_metric (int): Current metric count.
            target_metric (int): Desired goal target count.
            avg_per_day (float): Average daily growth rate.

        Returns:
            int: Total days required to reach target.
        """
        if current_metric >= target_metric or avg_per_day <= 0:
            return 0

        remaining = target_metric - current_metric
        return math.ceil(remaining / avg_per_day)


if __name__ == "__main__":
    calc = CreditCardRepaymentCalculator(initial_balance=5000, annual_interest_rate=0.26, monthly_payment=204)
    sched, total_interest = calc.calculate_repayment_schedule(datetime.date(2026, 1, 1))

    print(f"Credit Card Repayment: {len(sched)} months required.")
    print(f"Total Interest Paid : £{total_interest}")

    weight_tracker = WeightLossGoalTracker(current_weight=100.0, target_weight=75.0, avg_loss_per_week=0.8)
    end_dt, weeks = weight_tracker.estimate_completion_date(datetime.date.today())
    print(f"Weight Loss Milestone : {weeks} weeks needed (Est Date: {end_dt})")
