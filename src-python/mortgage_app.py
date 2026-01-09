"""
Main Mortgage Calculator Application
Integrates all modules and handles file I/O
"""

import json
import sys
from pathlib import Path

from validator import MortgageValidator
from calculator import MortgageCalculator
from amortization import AmortizationSchedule
from features import (
    LoanFeatures, PropertyTaxCalculator, InsuranceCalculator,
    PMICalculator, HOACalculator, TotalHousingPaymentCalculator
)
from output import (
    LoanSummaryReporter, KeyMetricsReporter, AmortizationScheduleReporter,
    WarningMessageGenerator, ErrorMessageFormatter
)


class MortgageApplication:
    """Main application class that orchestrates the mortgage calculation"""

    def __init__(self, input_file='input/loan_params.json'):
        self.input_file = input_file
        self.params = {}
        self.validator = MortgageValidator()
        self.calculator = None
        self.amortization = None
        self.loan_features = None

    def load_input(self):
        """
        Load loan parameters from JSON input file
        REQ-VAL-020: Trim whitespace from inputs
        """
        try:
            with open(self.input_file, 'r') as f:
                self.params = json.load(f)

            # REQ-VAL-020: Trim whitespace from string inputs
            for key, value in self.params.items():
                self.params[key] = self.validator.trim_whitespace(value)

            return True
        except FileNotFoundError:
            print(f"Error: Input file '{self.input_file}' not found.")
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in input file: {e}")
            return False

    def validate_input(self):
        """
        Validate all input parameters
        Returns list of validation errors (empty if valid)
        """
        errors = self.validator.validate_all(self.params)
        return errors

    def initialize_calculator(self):
        """Initialize calculator with validated parameters"""
        # REQ-CALC series: Core calculator
        self.calculator = MortgageCalculator(
            principal=self.params['principal'],
            annual_interest_rate=self.params['annual_interest_rate'],
            loan_term_years=self.params['loan_term_years']
        )

        # REQ-LOAN-013 through REQ-LOAN-016: Loan features
        property_value = self.params.get('property_value')
        if property_value:
            self.loan_features = LoanFeatures(
                principal=self.params['principal'],
                property_value=property_value
            )

    def initialize_amortization(self):
        """
        Initialize amortization schedule
        REQ-AMORT series
        """
        start_date = self.params.get('start_date')
        self.amortization = AmortizationSchedule(
            calculator=self.calculator,
            start_date=start_date
        )

    def generate_schedule(self):
        """
        Generate amortization schedule with optional extra payments
        REQ-AMORT-017: Support extra payments
        """
        extra_payments = {}

        # REQ-FEAT-016, REQ-FEAT-017: One-time or recurring extra payments
        if self.params.get('extra_monthly_payment'):
            # Apply to all payments
            for pmt_num in range(1, self.calculator.num_payments + 1):
                extra_payments[pmt_num] = self.params['extra_monthly_payment']

        # Generate schedule
        schedule = self.amortization.generate_schedule(extra_payments)

        # REQ-AMORT-011, REQ-AMORT-012, REQ-AMORT-013: Add running totals
        self.amortization.add_running_totals()

        return schedule

    def calculate_total_housing_payment(self):
        """
        Calculate total monthly housing payment including all components
        REQ-FEAT-003, REQ-FEAT-007, REQ-FEAT-009, REQ-FEAT-015
        """
        monthly_payment = self.calculator.calculate_monthly_payment()

        # Initialize PMI calculator if applicable
        pmi_calculator = None
        if self.params.get('property_value') and self.params.get('pmi_rate'):
            pmi_calculator = PMICalculator(
                principal=self.params['principal'],
                property_value=self.params['property_value'],
                pmi_rate=self.params['pmi_rate']
            )

        # Calculate total housing payment
        housing_calc = TotalHousingPaymentCalculator()
        components = housing_calc.calculate_total(
            monthly_pi_payment=monthly_payment,
            annual_property_tax=self.params.get('annual_property_tax'),
            annual_insurance=self.params.get('annual_insurance'),
            pmi_calculator=pmi_calculator,
            monthly_hoa=self.params.get('monthly_hoa')
        )

        return components, pmi_calculator

    def generate_reports(self, output_dir='output'):
        """
        Generate all output reports
        REQ-OUT series: Output and reporting
        """
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Generate amortization schedule
        schedule = self.generate_schedule()

        # Calculate total housing payment
        housing_components, pmi_calculator = self.calculate_total_housing_payment()

        # Generate warnings
        # REQ-OUT-027, REQ-OUT-028, REQ-OUT-029
        warning_gen = WarningMessageGenerator()

        pmi_removal = None
        if pmi_calculator and pmi_calculator.is_pmi_required():
            pmi_removal = pmi_calculator.find_pmi_removal_payment(schedule)

        warnings = warning_gen.check_and_generate_warnings(
            self.params,
            pmi_removal_payment=pmi_removal
        )

        # Build full report
        report_lines = []

        # REQ-OUT-001: Loan summary
        summary_reporter = LoanSummaryReporter(self.calculator, self.loan_features)
        report_lines.append(summary_reporter.generate_summary())

        # REQ-OUT-005, REQ-OUT-006, REQ-OUT-007: Detailed breakdown
        report_lines.append(summary_reporter.generate_detailed_breakdown())

        # REQ-OUT-017, REQ-OUT-018, REQ-OUT-019, REQ-OUT-020: Key metrics
        metrics_reporter = KeyMetricsReporter(self.calculator, housing_components)
        report_lines.append(metrics_reporter.generate_metrics())

        # Warnings and notices
        if warnings:
            report_lines.append(warning_gen.format_warnings())

        # Write summary report
        summary_file = Path(output_dir) / 'loan_summary.txt'
        with open(summary_file, 'w') as f:
            f.write('\n'.join(report_lines))

        print(f"Loan summary written to: {summary_file}")

        # REQ-OUT-008, REQ-OUT-009: Amortization schedule table
        schedule_reporter = AmortizationScheduleReporter(schedule)

        # Write full schedule
        schedule_file = Path(output_dir) / 'amortization_schedule.txt'
        with open(schedule_file, 'w') as f:
            f.write(schedule_reporter.generate_table())

        print(f"Amortization schedule written to: {schedule_file}")

        # REQ-OUT-011: Export to CSV
        csv_file = Path(output_dir) / 'amortization_schedule.csv'
        schedule_reporter.export_to_csv(csv_file)
        print(f"CSV export written to: {csv_file}")

        # REQ-AMORT-009: Annual summary
        annual_summary = self.amortization.generate_annual_summary()
        if annual_summary:
            annual_file = Path(output_dir) / 'annual_summary.txt'
            with open(annual_file, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write("ANNUAL SUMMARY\n")
                f.write("=" * 60 + "\n\n")

                for year_data in annual_summary:
                    f.write(f"Year {year_data['year']}:\n")
                    f.write(f"  Payments Made: {year_data['num_payments']}\n")
                    f.write(f"  Total Principal: ${year_data['total_principal']:,.2f}\n")
                    f.write(f"  Total Interest: ${year_data['total_interest']:,.2f}\n")
                    f.write(f"  Total Paid: ${year_data['total_payments']:,.2f}\n")
                    f.write("\n")

            print(f"Annual summary written to: {annual_file}")

        # Write detailed JSON output for programmatic access
        json_file = Path(output_dir) / 'calculation_results.json'
        results = {
            'summary': self.calculator.get_summary(),
            'housing_components': housing_components,
            'schedule': schedule,
            'annual_summary': annual_summary
        }

        # Convert any non-serializable types
        results_json = json.dumps(results, indent=2, default=str)
        with open(json_file, 'w') as f:
            f.write(results_json)

        print(f"JSON results written to: {json_file}")

        print("\nAll reports generated successfully!")

    def run(self):
        """Main execution flow"""
        print("=" * 60)
        print("MORTGAGE CALCULATOR")
        print("=" * 60)
        print()

        # Load input
        print(f"Loading input from: {self.input_file}")
        if not self.load_input():
            return 1

        # Validate input
        print("Validating input parameters...")
        errors = self.validate_input()

        if errors:
            # REQ-OUT-026: Display clear error messages
            # REQ-VAL-021: Report all errors
            error_formatter = ErrorMessageFormatter()
            print(error_formatter.format_errors(errors))
            return 1

        print("✓ Input validation passed")
        print()

        # Initialize calculator
        self.initialize_calculator()
        self.initialize_amortization()

        # Generate reports
        print("Generating reports...")
        self.generate_reports()

        return 0


def main():
    """Entry point"""
    # Check for custom input file
    input_file = 'input/loan_params.json'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    app = MortgageApplication(input_file)
    exit_code = app.run()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
