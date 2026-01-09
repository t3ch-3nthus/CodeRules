"""
Additional Features Module
Implements REQ-FEAT-001 through REQ-FEAT-031 and REQ-LOAN-013 through REQ-LOAN-016
"""


class LoanFeatures:
    """Manages additional loan features like PMI, taxes, insurance, etc."""

    def __init__(self, principal, property_value=None):
        """
        Initialize loan features

        Args:
            principal: Loan principal amount
            property_value: Property value (for LTV calculation)
        """
        self.principal = principal
        self.property_value = property_value

    def calculate_ltv(self):
        """
        REQ-LOAN-013: Calculate loan-to-value ratio
        LTV = (principal / property value) × 100
        REQ-LOAN-015: Express as percentage rounded to 2 decimal places
        """
        if self.property_value is None or self.property_value == 0:
            return None

        ltv = (self.principal / self.property_value) * 100
        # REQ-LOAN-015: Round to 2 decimal places
        return round(ltv, 2)

    def calculate_principal_from_down_payment(self, property_value, down_payment,
                                             down_payment_is_percentage=False):
        """
        REQ-LOAN-014: Calculate principal from property value and down payment
        REQ-LOAN-016: Support down payment as dollar amount or percentage

        Args:
            property_value: Property value
            down_payment: Down payment amount or percentage
            down_payment_is_percentage: True if down_payment is a percentage

        Returns:
            float: Calculated principal
        """
        if down_payment_is_percentage:
            # REQ-LOAN-016: Convert percentage to amount
            down_payment_amount = property_value * (down_payment / 100)
        else:
            down_payment_amount = down_payment

        # REQ-LOAN-014: Principal = property value - down payment
        principal = property_value - down_payment_amount
        return round(principal, 2)


class PropertyTaxCalculator:
    """Property tax calculations - REQ-FEAT-001 through REQ-FEAT-004"""

    @staticmethod
    def calculate_monthly_property_tax(annual_property_tax):
        """
        REQ-FEAT-001: Accept annual property tax amount
        REQ-FEAT-002: Calculate monthly amount by dividing by 12
        REQ-FEAT-004: Round to 2 decimal places
        """
        if annual_property_tax is None:
            return 0

        # REQ-FEAT-002: Divide by 12
        monthly_tax = annual_property_tax / 12

        # REQ-FEAT-004: Round to 2 decimal places
        return round(monthly_tax, 2)


class InsuranceCalculator:
    """Homeowners insurance calculations - REQ-FEAT-005 through REQ-FEAT-008"""

    @staticmethod
    def calculate_monthly_insurance(annual_insurance):
        """
        REQ-FEAT-005: Accept annual homeowners insurance premium
        REQ-FEAT-006: Calculate monthly amount by dividing by 12
        REQ-FEAT-008: Round to 2 decimal places
        """
        if annual_insurance is None:
            return 0

        # REQ-FEAT-006: Divide by 12
        monthly_insurance = annual_insurance / 12

        # REQ-FEAT-008: Round to 2 decimal places
        return round(monthly_insurance, 2)


class PMICalculator:
    """Private Mortgage Insurance calculations - REQ-FEAT-009 through REQ-FEAT-013"""

    def __init__(self, principal, property_value, pmi_rate):
        """
        Args:
            principal: Loan amount
            property_value: Original property value
            pmi_rate: Annual PMI rate as percentage (e.g., 0.5 for 0.5%)
        """
        self.principal = principal
        self.property_value = property_value
        self.pmi_rate = pmi_rate
        self.original_ltv = (principal / property_value * 100) if property_value else 0

    def is_pmi_required(self, current_balance=None):
        """
        REQ-FEAT-009: If LTV > 80%, PMI is required
        REQ-FEAT-012: Remove PMI when balance falls below 80% of original property value
        REQ-EDGE-025: Handle exact 80% LTV boundary
        REQ-EDGE-027: Handle rounding at 80% threshold
        """
        if current_balance is None:
            current_balance = self.principal

        if self.property_value is None or self.property_value == 0:
            return False

        current_ltv = (current_balance / self.property_value) * 100

        # REQ-EDGE-025: At exactly 80%, PMI is not required
        # REQ-FEAT-009: Greater than 80% requires PMI
        return current_ltv > 80.0

    def calculate_monthly_pmi(self):
        """
        REQ-FEAT-010: Calculate monthly PMI = (principal × annual PMI rate) / 12
        REQ-FEAT-011: Support PMI rates between 0.1% and 2.0%
        """
        if not self.is_pmi_required():
            return 0

        # REQ-FEAT-011: Validate PMI rate range (0.1% to 2.0%)
        if self.pmi_rate < 0.1 or self.pmi_rate > 2.0:
            return 0

        # REQ-FEAT-010: Calculate monthly PMI
        annual_pmi = self.principal * (self.pmi_rate / 100)
        monthly_pmi = annual_pmi / 12

        return round(monthly_pmi, 2)

    def find_pmi_removal_payment(self, amortization_schedule):
        """
        REQ-FEAT-013: Track payment number when PMI is removed
        REQ-EDGE-026: Remove PMI when LTV drops to exactly 80%

        Args:
            amortization_schedule: List of payment dictionaries

        Returns:
            int: Payment number when PMI is removed, or None
        """
        for payment in amortization_schedule:
            balance = payment['remaining_balance']
            ltv = (balance / self.property_value * 100) if self.property_value else 100

            # REQ-EDGE-026 & REQ-EDGE-027: Remove at or below 80%
            if ltv <= 80.0:
                return payment['payment_number']

        return None


class HOACalculator:
    """HOA fee calculations - REQ-FEAT-014 through REQ-FEAT-015"""

    @staticmethod
    def get_monthly_hoa(monthly_hoa_fee):
        """
        REQ-FEAT-014: Accept monthly HOA fees
        REQ-FEAT-015: Add to total monthly housing payment
        """
        return monthly_hoa_fee if monthly_hoa_fee else 0


class ExtraPaymentCalculator:
    """Extra payment calculations - REQ-FEAT-016 through REQ-FEAT-021"""

    @staticmethod
    def apply_extra_payment(remaining_balance, extra_amount):
        """
        REQ-FEAT-019: Extra payments reduce only principal, not interest
        REQ-VAL-018: If extra payment exceeds balance, only apply what's needed

        Args:
            remaining_balance: Current loan balance
            extra_amount: Extra payment amount

        Returns:
            float: Actual extra amount applied
        """
        if extra_amount <= 0:
            return 0

        # REQ-VAL-018: Don't exceed remaining balance
        if extra_amount >= remaining_balance:
            return remaining_balance

        return extra_amount


class TotalHousingPaymentCalculator:
    """Calculates total monthly housing payment including all components"""

    def __init__(self):
        self.components = {}

    def calculate_total(self, monthly_pi_payment, annual_property_tax=None,
                       annual_insurance=None, pmi_calculator=None,
                       monthly_hoa=None):
        """
        REQ-FEAT-003: Add property tax to base payment
        REQ-FEAT-007: Add insurance to calculate total
        REQ-FEAT-015: Add HOA fees to calculate total
        REQ-FEAT-009: Include PMI if applicable

        Returns:
            dict: Breakdown of total housing payment
        """
        self.components = {
            'principal_and_interest': monthly_pi_payment,
            'property_tax': 0,
            'insurance': 0,
            'pmi': 0,
            'hoa': 0
        }

        # REQ-FEAT-003: Add property tax
        if annual_property_tax:
            self.components['property_tax'] = \
                PropertyTaxCalculator.calculate_monthly_property_tax(annual_property_tax)

        # REQ-FEAT-007: Add insurance
        if annual_insurance:
            self.components['insurance'] = \
                InsuranceCalculator.calculate_monthly_insurance(annual_insurance)

        # REQ-FEAT-009: Add PMI if applicable
        if pmi_calculator and pmi_calculator.is_pmi_required():
            self.components['pmi'] = pmi_calculator.calculate_monthly_pmi()

        # REQ-FEAT-015: Add HOA
        if monthly_hoa:
            self.components['hoa'] = HOACalculator.get_monthly_hoa(monthly_hoa)

        # Calculate total
        total = sum(self.components.values())
        self.components['total_monthly_payment'] = round(total, 2)

        return self.components


class EarlyPayoffCalculator:
    """Early payoff calculations - REQ-FEAT-022 through REQ-FEAT-024"""

    @staticmethod
    def calculate_payoff_amount(remaining_balance):
        """
        REQ-FEAT-024: Calculate lump sum to pay off loan immediately

        Args:
            remaining_balance: Current remaining balance

        Returns:
            float: Amount needed to pay off immediately
        """
        return round(remaining_balance, 2)
