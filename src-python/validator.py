"""
Input Validation Module
Implements REQ-VAL-001 through REQ-VAL-021
"""

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


class MortgageValidator:
    """Validates mortgage calculator inputs according to EARS specifications"""

    def __init__(self):
        self.errors = []

    def validate_all(self, params):
        """
        Validates all input parameters
        REQ-VAL-021: Report all errors, not just the first
        """
        self.errors = []

        self.validate_principal(params.get('principal'))
        self.validate_interest_rate(params.get('annual_interest_rate'))
        self.validate_loan_term(params.get('loan_term_years'))

        if params.get('property_value') is not None:
            self.validate_property_value(
                params.get('property_value'),
                params.get('down_payment')
            )

        if params.get('extra_monthly_payment') is not None:
            self.validate_extra_payment(params.get('extra_monthly_payment'))

        # REQ-VAL-019: Validate all numeric inputs are finite and not NaN
        self._validate_numeric_types(params)

        return self.errors

    def validate_principal(self, principal):
        """
        Validates principal amount
        REQ-VAL-001, REQ-VAL-002, REQ-VAL-003, REQ-VAL-004
        """
        # REQ-VAL-004: Check if null or undefined
        if principal is None:
            self.errors.append("Principal amount is required")
            return

        # REQ-VAL-019: Check if valid number
        if not isinstance(principal, (int, float)) or not self._is_finite(principal):
            self.errors.append("Principal amount must be a valid number")
            return

        # REQ-VAL-003: Check if positive
        if principal <= 0:
            self.errors.append("Principal amount must be a positive number")
            return

        # REQ-VAL-001: Check minimum
        if principal < 1000:
            self.errors.append("Principal amount must be at least $1,000")
            return

        # REQ-VAL-002: Check maximum
        if principal > 10000000:
            self.errors.append("Principal amount cannot exceed $10,000,000")
            return

    def validate_interest_rate(self, rate):
        """
        Validates interest rate
        REQ-VAL-005, REQ-VAL-006, REQ-VAL-007, REQ-VAL-008
        """
        # REQ-VAL-007: Check if null or undefined
        if rate is None:
            self.errors.append("Interest rate is required")
            return

        # REQ-VAL-008: Check if valid number
        if not isinstance(rate, (int, float)) or not self._is_finite(rate):
            self.errors.append("Interest rate must be a valid number")
            return

        # REQ-VAL-005: Check if non-negative
        if rate < 0:
            self.errors.append("Interest rate cannot be negative")
            return

        # REQ-VAL-006: Check maximum
        if rate > 20:
            self.errors.append("Interest rate cannot exceed 20%")
            return

    def validate_loan_term(self, term):
        """
        Validates loan term
        REQ-VAL-009, REQ-VAL-010, REQ-VAL-011, REQ-VAL-012, REQ-VAL-013
        """
        # REQ-VAL-012: Check if null or undefined
        if term is None:
            self.errors.append("Loan term is required")
            return

        # REQ-VAL-019: Check if valid number
        if not isinstance(term, (int, float)) or not self._is_finite(term):
            self.errors.append("Loan term must be a valid number")
            return

        # REQ-VAL-011: Check if positive
        if term <= 0:
            self.errors.append("Loan term must be a positive number")
            return

        # REQ-VAL-009: Check minimum
        if term < 1:
            self.errors.append("Loan term must be at least 1 year")
            return

        # REQ-VAL-010: Check maximum
        if term > 40:
            self.errors.append("Loan term cannot exceed 40 years")
            return

        # REQ-VAL-013: Fractional years are accepted (no validation needed)

    def validate_property_value(self, property_value, down_payment):
        """
        Validates property value and down payment
        REQ-VAL-014, REQ-VAL-015, REQ-VAL-016
        """
        if property_value is None:
            return

        # REQ-VAL-014: Property value must be greater than 0
        if property_value <= 0:
            self.errors.append("Property value must be greater than 0")
            return

        if down_payment is not None:
            # REQ-VAL-016: Down payment cannot be negative
            if down_payment < 0:
                self.errors.append("Down payment cannot be negative")
                return

            # REQ-VAL-015: Down payment must be less than property value
            if down_payment >= property_value:
                self.errors.append("Down payment must be less than property value")
                return

    def validate_extra_payment(self, extra_payment):
        """
        Validates extra payment amount
        REQ-VAL-017
        """
        if extra_payment is None:
            return

        # REQ-VAL-017: Extra payment cannot be negative
        if extra_payment < 0:
            self.errors.append("Extra payment amount cannot be negative")
            return

    def _is_finite(self, value):
        """
        REQ-VAL-019: Validate that numeric inputs are finite and not NaN
        """
        import math
        return math.isfinite(value)

    def _validate_numeric_types(self, params):
        """
        REQ-VAL-019: Validate all numeric inputs are finite and not NaN
        """
        numeric_fields = [
            'principal', 'annual_interest_rate', 'loan_term_years',
            'property_value', 'down_payment', 'annual_property_tax',
            'annual_insurance', 'pmi_rate', 'monthly_hoa',
            'extra_monthly_payment'
        ]

        for field in numeric_fields:
            value = params.get(field)
            if value is not None and isinstance(value, (int, float)):
                if not self._is_finite(value):
                    self.errors.append(f"{field} must be a finite number and not NaN")

    @staticmethod
    def trim_whitespace(value):
        """
        REQ-VAL-020: Trim whitespace from string inputs
        """
        if isinstance(value, str):
            return value.strip()
        return value
