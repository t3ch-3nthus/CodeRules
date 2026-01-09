"""
Core Mortgage Calculations Module
Implements REQ-CALC-001 through REQ-CALC-013
"""

import math


class MortgageCalculator:
    """Core mortgage calculation functions"""

    def __init__(self, principal, annual_interest_rate, loan_term_years):
        """
        Initialize calculator with basic loan parameters

        Args:
            principal: Loan principal amount
            annual_interest_rate: Annual interest rate as percentage (e.g., 4.5 for 4.5%)
            loan_term_years: Loan term in years
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

        # REQ-CALC-002: Convert annual rate to monthly rate
        self.monthly_interest_rate = self._convert_to_monthly_rate(annual_interest_rate)

        # REQ-CALC-003: Convert years to months
        self.num_payments = self._convert_to_months(loan_term_years)

    def _convert_to_monthly_rate(self, annual_rate):
        """
        REQ-CALC-002: Convert annual interest rate to monthly rate by dividing by 12
        REQ-CALC-009: Convert APR percentage to decimal by dividing by 100
        """
        # Convert percentage to decimal, then to monthly rate
        return (annual_rate / 100) / 12

    def _convert_to_months(self, years):
        """
        REQ-CALC-003: Convert loan term in years to number of monthly payments
        REQ-EDGE-012: Handle fractional years
        REQ-EDGE-013: Round to nearest whole month if needed
        """
        months = years * 12
        return round(months)

    def calculate_monthly_payment(self):
        """
        REQ-CALC-001: Calculate monthly payment using standard mortgage formula
        M = P[r(1+r)^n]/[(1+r)^n-1]

        REQ-CALC-004: Handle 0% interest rate special case
        REQ-CALC-005: Round result to 2 decimal places
        """
        P = self.principal
        r = self.monthly_interest_rate
        n = self.num_payments

        # REQ-CALC-004: Special case for 0% interest
        if self.annual_interest_rate == 0 or r == 0:
            monthly_payment = P / n
        else:
            # REQ-CALC-001: Standard mortgage formula
            monthly_payment = P * (r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

        # REQ-CALC-005: Round to 2 decimal places
        return round(monthly_payment, 2)

    def calculate_total_amount_paid(self, monthly_payment=None):
        """
        REQ-CALC-007: Calculate total amount paid
        Total = monthly payment × number of payments
        REQ-CALC-008: Round to 2 decimal places
        """
        if monthly_payment is None:
            monthly_payment = self.calculate_monthly_payment()

        total = monthly_payment * self.num_payments

        # REQ-CALC-008: Round to 2 decimal places
        return round(total, 2)

    def calculate_total_interest(self, monthly_payment=None):
        """
        REQ-CALC-006: Calculate total interest paid over life of loan
        Total Interest = (monthly payment × number of payments) - principal
        REQ-CALC-008: Round to 2 decimal places
        """
        if monthly_payment is None:
            monthly_payment = self.calculate_monthly_payment()

        total_paid = self.calculate_total_amount_paid(monthly_payment)
        total_interest = total_paid - self.principal

        # REQ-CALC-008: Round to 2 decimal places
        return round(total_interest, 2)

    def calculate_payment_breakdown(self, remaining_balance, monthly_payment=None):
        """
        Calculate principal and interest portions of a payment

        REQ-CALC-011: Interest portion = remaining balance × monthly interest rate
        REQ-CALC-012: Principal portion = monthly payment - interest portion
        REQ-CALC-013: Ensure principal portion does not exceed remaining balance

        Args:
            remaining_balance: Current remaining loan balance
            monthly_payment: Monthly payment amount (optional)

        Returns:
            tuple: (principal_portion, interest_portion)
        """
        if monthly_payment is None:
            monthly_payment = self.calculate_monthly_payment()

        # REQ-CALC-011: Calculate interest portion
        interest_portion = remaining_balance * self.monthly_interest_rate
        interest_portion = round(interest_portion, 2)

        # REQ-CALC-012: Calculate principal portion
        principal_portion = monthly_payment - interest_portion
        principal_portion = round(principal_portion, 2)

        # REQ-CALC-013: Ensure principal doesn't exceed remaining balance
        if principal_portion > remaining_balance:
            principal_portion = remaining_balance
            interest_portion = monthly_payment - principal_portion

        return (principal_portion, interest_portion)

    def get_summary(self):
        """Get a summary of key loan metrics"""
        monthly_payment = self.calculate_monthly_payment()
        total_paid = self.calculate_total_amount_paid(monthly_payment)
        total_interest = self.calculate_total_interest(monthly_payment)

        return {
            'principal': self.principal,
            'annual_interest_rate': self.annual_interest_rate,
            'monthly_interest_rate': self.monthly_interest_rate,
            'loan_term_years': self.loan_term_years,
            'num_payments': self.num_payments,
            'monthly_payment': monthly_payment,
            'total_amount_paid': total_paid,
            'total_interest_paid': total_interest
        }
