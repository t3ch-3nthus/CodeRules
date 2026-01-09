"""
Amortization Schedule Module
Implements REQ-AMORT-001 through REQ-AMORT-020
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


class AmortizationSchedule:
    """Generates and manages amortization schedules"""

    def __init__(self, calculator, start_date=None):
        """
        Initialize amortization schedule generator

        Args:
            calculator: MortgageCalculator instance
            start_date: Loan start date (string or datetime)
        """
        self.calculator = calculator
        self.start_date = self._parse_start_date(start_date)
        self.schedule = []

    def _parse_start_date(self, start_date):
        """
        Parse start date or use default
        REQ-AMORT-007: Use first day of following month if no date provided
        """
        if start_date is None:
            # REQ-AMORT-007: Default to first day of next month
            today = datetime.now()
            if today.month == 12:
                return datetime(today.year + 1, 1, 1)
            else:
                return datetime(today.year, today.month + 1, 1)

        if isinstance(start_date, str):
            return datetime.fromisoformat(start_date)

        return start_date

    def _calculate_next_payment_date(self, current_date, payment_num):
        """
        REQ-AMORT-005: Calculate payment dates as monthly intervals
        REQ-AMORT-006: Handle months without certain days (e.g., Feb 30)
        REQ-EDGE-028, REQ-EDGE-029, REQ-EDGE-030: Handle edge cases for dates
        """
        # Add months to start date
        next_date = self.start_date + relativedelta(months=payment_num)

        # REQ-AMORT-006 & REQ-EDGE-028/029: If day doesn't exist, use last day of month
        # relativedelta handles this automatically

        return next_date

    def generate_schedule(self, extra_payments=None):
        """
        REQ-AMORT-001: Generate amortization schedule showing breakdown of each payment
        REQ-AMORT-002: Include payment number, date, amount, principal, interest, balance
        REQ-AMORT-003: Calculate remaining balance after each payment
        REQ-AMORT-004: Ensure final balance equals $0.00 (within $0.01)

        Args:
            extra_payments: Dict of {payment_number: extra_amount} (optional)

        Returns:
            list: Schedule with payment details
        """
        self.schedule = []
        monthly_payment = self.calculator.calculate_monthly_payment()
        remaining_balance = self.calculator.principal

        extra_payments = extra_payments or {}

        # REQ-AMORT-010: Number payments starting from 1
        for payment_num in range(1, self.calculator.num_payments + 1):
            # REQ-AMORT-005: Calculate payment date
            payment_date = self._calculate_next_payment_date(
                self.start_date, payment_num - 1
            )

            # Calculate principal and interest breakdown
            principal_portion, interest_portion = \
                self.calculator.calculate_payment_breakdown(
                    remaining_balance, monthly_payment
                )

            # Handle extra payments
            # REQ-AMORT-017, REQ-AMORT-019: Track extra payments
            extra_amount = extra_payments.get(payment_num, 0)
            total_payment = monthly_payment + extra_amount

            # REQ-AMORT-015: Adjust final payment if needed due to rounding
            # REQ-EDGE-018: Ensure loan is fully paid
            if payment_num == self.calculator.num_payments or \
               (principal_portion + extra_amount) >= remaining_balance:
                # Final payment - pay off exact remaining balance
                principal_portion = remaining_balance
                total_payment = principal_portion + interest_portion
                extra_amount = 0  # Absorbed into principal portion

            # REQ-AMORT-003: Calculate remaining balance
            remaining_balance = remaining_balance - principal_portion - extra_amount
            remaining_balance = max(0, round(remaining_balance, 2))

            # REQ-AMORT-014: Round all monetary values to 2 decimal places
            payment_info = {
                'payment_number': payment_num,  # REQ-AMORT-010
                'payment_date': payment_date.strftime('%Y-%m-%d'),  # REQ-AMORT-002
                'payment_amount': round(total_payment, 2),  # REQ-AMORT-002
                'principal': round(principal_portion, 2),  # REQ-AMORT-002
                'interest': round(interest_portion, 2),  # REQ-AMORT-002
                'extra_payment': round(extra_amount, 2),  # REQ-AMORT-019
                'remaining_balance': remaining_balance  # REQ-AMORT-002
            }

            self.schedule.append(payment_info)

            # REQ-AMORT-004 & REQ-AMORT-017: Stop if loan is paid off early
            if remaining_balance == 0:
                break

        # REQ-AMORT-004: Verify final balance is $0.00 (within $0.01)
        if self.schedule:
            final_balance = self.schedule[-1]['remaining_balance']
            assert final_balance < 0.01, f"Final balance {final_balance} exceeds tolerance"

        return self.schedule

    def generate_annual_summary(self):
        """
        REQ-AMORT-009: Generate annual summaries showing total principal and interest per year

        Returns:
            list: Annual summaries
        """
        if not self.schedule:
            return []

        annual_summaries = {}

        for payment in self.schedule:
            year = payment['payment_date'][:4]  # Extract year

            if year not in annual_summaries:
                annual_summaries[year] = {
                    'year': year,
                    'total_principal': 0,
                    'total_interest': 0,
                    'total_payments': 0,
                    'num_payments': 0
                }

            annual_summaries[year]['total_principal'] += payment['principal']
            annual_summaries[year]['total_interest'] += payment['interest']
            annual_summaries[year]['total_payments'] += payment['payment_amount']
            annual_summaries[year]['num_payments'] += 1

        # Round all values
        for year_data in annual_summaries.values():
            year_data['total_principal'] = round(year_data['total_principal'], 2)
            year_data['total_interest'] = round(year_data['total_interest'], 2)
            year_data['total_payments'] = round(year_data['total_payments'], 2)

        return list(annual_summaries.values())

    def add_running_totals(self):
        """
        REQ-AMORT-011: Track cumulative principal paid
        REQ-AMORT-012: Track cumulative interest paid
        REQ-AMORT-013: Display cumulative amounts
        """
        cumulative_principal = 0
        cumulative_interest = 0

        for payment in self.schedule:
            cumulative_principal += payment['principal']
            cumulative_interest += payment['interest']

            # REQ-AMORT-013: Add to schedule
            payment['cumulative_principal'] = round(cumulative_principal, 2)
            payment['cumulative_interest'] = round(cumulative_interest, 2)

        return self.schedule

    def verify_schedule_integrity(self):
        """
        REQ-AMORT-016: Verify sum of principal portions equals original principal (within $0.01)

        Returns:
            bool: True if schedule is valid
        """
        if not self.schedule:
            return False

        total_principal_paid = sum(payment['principal'] for payment in self.schedule)
        difference = abs(total_principal_paid - self.calculator.principal)

        # REQ-AMORT-016: Within $0.01 tolerance
        return difference < 0.01

    def calculate_extra_payment_impact(self, extra_payments):
        """
        REQ-AMORT-017: Recalculate schedule with extra payments
        REQ-AMORT-018: Reduce balance and shorten term or reduce payments
        REQ-AMORT-020: Calculate time saved and interest saved

        Args:
            extra_payments: Dict of {payment_number: extra_amount}

        Returns:
            dict: Impact metrics
        """
        # Generate schedule without extra payments
        self.generate_schedule()
        original_payments = len(self.schedule)
        original_interest = sum(p['interest'] for p in self.schedule)

        # Generate schedule with extra payments
        self.generate_schedule(extra_payments)
        new_payments = len(self.schedule)
        new_interest = sum(p['interest'] for p in self.schedule)

        # REQ-AMORT-020: Calculate savings
        return {
            'payments_saved': original_payments - new_payments,
            'months_saved': original_payments - new_payments,
            'interest_saved': round(original_interest - new_interest, 2),
            'original_total_interest': round(original_interest, 2),
            'new_total_interest': round(new_interest, 2)
        }
