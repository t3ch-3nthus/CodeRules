"""
Output and Reporting Module
Implements REQ-OUT-001 through REQ-OUT-032
"""

import csv
from datetime import datetime


class OutputFormatter:
    """Formats and displays mortgage calculation outputs"""

    @staticmethod
    def format_currency(amount):
        """
        REQ-OUT-002: Format with dollar sign and comma separators
        REQ-OUT-004: Use comma separators every three digits
        REQ-OUT-030: Round to 2 decimal places
        """
        return f"${amount:,.2f}"

    @staticmethod
    def format_percentage(value, decimal_places=2):
        """
        REQ-OUT-003: Format with percent sign and appropriate decimal places
        REQ-OUT-031: 3 decimals for interest rates, 2 for other percentages
        """
        return f"{value:.{decimal_places}f}%"

    @staticmethod
    def format_date(date_str):
        """
        REQ-OUT-032: Use consistent date formatting
        """
        return date_str  # Already in YYYY-MM-DD format from amortization module


class LoanSummaryReporter:
    """Generates loan summary reports - REQ-OUT-001 through REQ-OUT-007"""

    def __init__(self, calculator, loan_features=None):
        self.calculator = calculator
        self.loan_features = loan_features
        self.formatter = OutputFormatter()

    def generate_summary(self):
        """
        REQ-OUT-001: Display loan summary with all key information
        """
        summary = self.calculator.get_summary()

        output_lines = []
        output_lines.append("=" * 60)
        output_lines.append("MORTGAGE LOAN SUMMARY")
        output_lines.append("=" * 60)
        output_lines.append("")

        # REQ-OUT-001: Principal amount
        output_lines.append(f"Principal Amount: {self.formatter.format_currency(summary['principal'])}")

        # REQ-OUT-001: Annual interest rate
        # REQ-OUT-031: 3 decimal places for interest rates
        output_lines.append(f"Annual Interest Rate: {self.formatter.format_percentage(summary['annual_interest_rate'], 3)}")

        # REQ-OUT-001: Loan term
        output_lines.append(f"Loan Term: {summary['loan_term_years']} years ({summary['num_payments']} months)")

        output_lines.append("")
        output_lines.append("-" * 60)

        # REQ-OUT-001: Monthly payment
        output_lines.append(f"Monthly Payment (P&I): {self.formatter.format_currency(summary['monthly_payment'])}")

        # REQ-OUT-001: Total amount paid
        output_lines.append(f"Total Amount Paid: {self.formatter.format_currency(summary['total_amount_paid'])}")

        # REQ-OUT-001: Total interest paid
        output_lines.append(f"Total Interest Paid: {self.formatter.format_currency(summary['total_interest_paid'])}")

        output_lines.append("")

        return "\n".join(output_lines)

    def generate_detailed_breakdown(self):
        """
        REQ-OUT-005: Display first payment breakdown
        REQ-OUT-006: Display last payment breakdown
        REQ-OUT-007: Show percentage of payment going to principal vs interest
        """
        summary = self.calculator.get_summary()
        monthly_payment = summary['monthly_payment']

        output_lines = []
        output_lines.append("=" * 60)
        output_lines.append("DETAILED PAYMENT BREAKDOWN")
        output_lines.append("=" * 60)
        output_lines.append("")

        # REQ-OUT-005: First payment breakdown
        first_principal, first_interest = self.calculator.calculate_payment_breakdown(
            self.calculator.principal, monthly_payment
        )

        output_lines.append("FIRST PAYMENT:")
        output_lines.append(f"  Principal Portion: {self.formatter.format_currency(first_principal)}")
        output_lines.append(f"  Interest Portion: {self.formatter.format_currency(first_interest)}")

        # REQ-OUT-007: Percentage breakdown
        if monthly_payment > 0:
            principal_pct = (first_principal / monthly_payment) * 100
            interest_pct = (first_interest / monthly_payment) * 100
            output_lines.append(f"  Principal %: {self.formatter.format_percentage(principal_pct)}")
            output_lines.append(f"  Interest %: {self.formatter.format_percentage(interest_pct)}")

        output_lines.append("")

        # REQ-OUT-006: Last payment breakdown (approximate)
        # Calculate approximate last payment balance
        total_principal = first_principal * self.calculator.num_payments
        approx_last_balance = max(monthly_payment, self.calculator.principal * 0.01)

        last_principal, last_interest = self.calculator.calculate_payment_breakdown(
            approx_last_balance, monthly_payment
        )

        output_lines.append("APPROXIMATE LAST PAYMENT:")
        output_lines.append(f"  Principal Portion: {self.formatter.format_currency(last_principal)}")
        output_lines.append(f"  Interest Portion: {self.formatter.format_currency(last_interest)}")

        # REQ-OUT-007: Percentage breakdown
        if monthly_payment > 0:
            principal_pct = (last_principal / monthly_payment) * 100
            interest_pct = (last_interest / monthly_payment) * 100
            output_lines.append(f"  Principal %: {self.formatter.format_percentage(principal_pct)}")
            output_lines.append(f"  Interest %: {self.formatter.format_percentage(interest_pct)}")

        output_lines.append("")

        return "\n".join(output_lines)


class KeyMetricsReporter:
    """Generate key metrics - REQ-OUT-017 through REQ-OUT-020"""

    def __init__(self, calculator, total_housing_components=None):
        self.calculator = calculator
        self.total_housing_components = total_housing_components
        self.formatter = OutputFormatter()

    def generate_metrics(self):
        """Generate key loan metrics"""
        summary = self.calculator.get_summary()

        output_lines = []
        output_lines.append("=" * 60)
        output_lines.append("KEY METRICS")
        output_lines.append("=" * 60)
        output_lines.append("")

        # REQ-OUT-017: Interest-to-principal ratio
        if summary['principal'] > 0:
            ratio = summary['total_interest_paid'] / summary['principal']
            output_lines.append(f"Interest-to-Principal Ratio: {ratio:.4f}")

        # REQ-OUT-018: Total cost as percentage of principal
        if summary['principal'] > 0:
            cost_pct = (summary['total_amount_paid'] / summary['principal']) * 100
            output_lines.append(f"Total Cost (% of Principal): {self.formatter.format_percentage(cost_pct)}")

        # REQ-OUT-019: P&I payment
        output_lines.append(f"Monthly P&I Payment: {self.formatter.format_currency(summary['monthly_payment'])}")

        # REQ-OUT-020: Total housing payment if components provided
        if self.total_housing_components:
            total = self.total_housing_components.get('total_monthly_payment', 0)
            output_lines.append(f"Total Monthly Housing Payment: {self.formatter.format_currency(total)}")

            # Show breakdown
            output_lines.append("")
            output_lines.append("Housing Payment Breakdown:")
            for component, value in self.total_housing_components.items():
                if component != 'total_monthly_payment' and value > 0:
                    label = component.replace('_', ' ').title()
                    output_lines.append(f"  {label}: {self.formatter.format_currency(value)}")

        output_lines.append("")

        return "\n".join(output_lines)


class AmortizationScheduleReporter:
    """Generates amortization schedule reports - REQ-OUT-008 through REQ-OUT-012"""

    def __init__(self, amortization_schedule):
        self.schedule = amortization_schedule
        self.formatter = OutputFormatter()

    def generate_table(self, start_payment=None, end_payment=None):
        """
        REQ-OUT-008: Format as table with aligned columns
        REQ-OUT-009: Include column headers
        REQ-OUT-010: Allow filtering by payment range

        Args:
            start_payment: First payment number to include (optional)
            end_payment: Last payment number to include (optional)
        """
        if not self.schedule:
            return "No amortization schedule available.\n"

        output_lines = []
        output_lines.append("=" * 100)
        output_lines.append("AMORTIZATION SCHEDULE")
        output_lines.append("=" * 100)
        output_lines.append("")

        # REQ-OUT-009: Column headers
        header = f"{'Pmt#':<6} {'Date':<12} {'Payment':<15} {'Principal':<15} {'Interest':<15} {'Balance':<15}"
        output_lines.append(header)
        output_lines.append("-" * 100)

        # Filter schedule
        filtered_schedule = self.schedule
        if start_payment or end_payment:
            filtered_schedule = self._filter_by_range(start_payment, end_payment)

        # REQ-OUT-008: Format rows with aligned columns
        for payment in filtered_schedule:
            row = (
                f"{payment['payment_number']:<6} "
                f"{payment['payment_date']:<12} "
                f"{self.formatter.format_currency(payment['payment_amount']):<15} "
                f"{self.formatter.format_currency(payment['principal']):<15} "
                f"{self.formatter.format_currency(payment['interest']):<15} "
                f"{self.formatter.format_currency(payment['remaining_balance']):<15}"
            )
            output_lines.append(row)

        output_lines.append("")

        return "\n".join(output_lines)

    def _filter_by_range(self, start_payment, end_payment):
        """
        REQ-OUT-010: Filter schedule by payment range
        """
        filtered = []
        for payment in self.schedule:
            pmt_num = payment['payment_number']
            if start_payment and pmt_num < start_payment:
                continue
            if end_payment and pmt_num > end_payment:
                continue
            filtered.append(payment)
        return filtered

    def export_to_csv(self, filename):
        """
        REQ-OUT-011: Export schedule to CSV format
        """
        if not self.schedule:
            return False

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['payment_number', 'payment_date', 'payment_amount',
                         'principal', 'interest', 'remaining_balance']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for payment in self.schedule:
                row = {key: payment[key] for key in fieldnames}
                writer.writerow(row)

        return True


class WarningMessageGenerator:
    """Generates warning messages - REQ-OUT-026 through REQ-OUT-029"""

    def __init__(self):
        self.warnings = []

    def check_and_generate_warnings(self, loan_params, pmi_removal_payment=None):
        """
        Generate appropriate warnings based on loan parameters

        REQ-OUT-027: Warning for long loan terms (> 30 years)
        REQ-OUT-028: Warning for high interest rates (> 10%)
        REQ-OUT-029: Info message about PMI removal
        """
        self.warnings = []

        # REQ-OUT-027: Long loan term warning
        if loan_params.get('loan_term_years', 0) > 30:
            self.warnings.append("WARNING: Long loan terms result in significantly higher total interest paid")

        # REQ-OUT-028: High interest rate warning
        if loan_params.get('annual_interest_rate', 0) > 10:
            self.warnings.append("WARNING: This interest rate is higher than typical market rates")

        # REQ-OUT-029: PMI removal information
        if pmi_removal_payment:
            self.warnings.append(f"INFO: PMI will be removed after payment #{pmi_removal_payment}")

        return self.warnings

    def format_warnings(self):
        """Format warnings for display"""
        if not self.warnings:
            return ""

        output_lines = []
        output_lines.append("=" * 60)
        output_lines.append("NOTICES AND WARNINGS")
        output_lines.append("=" * 60)
        output_lines.append("")

        for warning in self.warnings:
            output_lines.append(warning)

        output_lines.append("")

        return "\n".join(output_lines)


class ErrorMessageFormatter:
    """Formats error messages - REQ-OUT-026"""

    @staticmethod
    def format_errors(errors):
        """
        REQ-OUT-026: Display clear, actionable error messages

        Args:
            errors: List of error message strings

        Returns:
            str: Formatted error output
        """
        if not errors:
            return ""

        output_lines = []
        output_lines.append("=" * 60)
        output_lines.append("VALIDATION ERRORS")
        output_lines.append("=" * 60)
        output_lines.append("")
        output_lines.append("The following errors were found:")
        output_lines.append("")

        for i, error in enumerate(errors, 1):
            output_lines.append(f"{i}. {error}")

        output_lines.append("")
        output_lines.append("Please correct these errors and try again.")
        output_lines.append("")

        return "\n".join(output_lines)
