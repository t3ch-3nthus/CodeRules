# Input Validation Specifications

## Principal Amount Validation

**REQ-VAL-001**: IF the principal amount is less than $1,000, THEN the system shall reject the input and display an error message "Principal amount must be at least $1,000".

**REQ-VAL-002**: IF the principal amount is greater than $10,000,000, THEN the system shall reject the input and display an error message "Principal amount cannot exceed $10,000,000".

**REQ-VAL-003**: IF the principal amount is not a positive number, THEN the system shall reject the input and display an error message "Principal amount must be a positive number".

**REQ-VAL-004**: IF the principal amount is null or undefined, THEN the system shall reject the input and display an error message "Principal amount is required".

## Interest Rate Validation

**REQ-VAL-005**: IF the annual interest rate is less than 0%, THEN the system shall reject the input and display an error message "Interest rate cannot be negative".

**REQ-VAL-006**: IF the annual interest rate is greater than 20%, THEN the system shall reject the input and display an error message "Interest rate cannot exceed 20%".

**REQ-VAL-007**: IF the interest rate is null or undefined, THEN the system shall reject the input and display an error message "Interest rate is required".

**REQ-VAL-008**: IF the interest rate is not a number, THEN the system shall reject the input and display an error message "Interest rate must be a valid number".

## Loan Term Validation

**REQ-VAL-009**: IF the loan term is less than 1 year, THEN the system shall reject the input and display an error message "Loan term must be at least 1 year".

**REQ-VAL-010**: IF the loan term is greater than 40 years, THEN the system shall reject the input and display an error message "Loan term cannot exceed 40 years".

**REQ-VAL-011**: IF the loan term is not a positive number, THEN the system shall reject the input and display an error message "Loan term must be a positive number".

**REQ-VAL-012**: IF the loan term is null or undefined, THEN the system shall reject the input and display an error message "Loan term is required".

**REQ-VAL-013**: The system shall accept loan terms as whole years or fractional years (e.g., 15.5 years).

## Property Value Validation

**REQ-VAL-014**: WHERE down payment calculation is included, IF the property value is less than or equal to 0, THEN the system shall reject the input and display an error message "Property value must be greater than 0".

**REQ-VAL-015**: WHERE down payment calculation is included, IF the down payment is greater than or equal to the property value, THEN the system shall reject the input and display an error message "Down payment must be less than property value".

**REQ-VAL-016**: WHERE down payment calculation is included, IF the down payment is negative, THEN the system shall reject the input and display an error message "Down payment cannot be negative".

## Additional Payment Validation

**REQ-VAL-017**: WHERE extra payment functionality is included, IF an extra payment amount is negative, THEN the system shall reject the input and display an error message "Extra payment amount cannot be negative".

**REQ-VAL-018**: WHERE extra payment functionality is included, IF an extra payment exceeds the remaining principal balance, THEN the system shall accept the payment but only apply the amount needed to pay off the loan.

## Data Type Validation

**REQ-VAL-019**: The system shall validate that all numeric inputs are finite numbers and not NaN (Not a Number).

**REQ-VAL-020**: The system shall trim whitespace from string inputs before validation and processing.

**REQ-VAL-021**: WHEN multiple validation errors exist, THEN the system shall report all errors to the user, not just the first error encountered.
