# Loan Types and Parameters Specifications

## Fixed-Rate Mortgages

**REQ-LOAN-001**: The system shall support fixed-rate mortgages where the interest rate remains constant throughout the loan term.

**REQ-LOAN-002**: The system shall support the following standard fixed-rate loan terms: 10, 15, 20, 25, and 30 years.

**REQ-LOAN-003**: The system shall allow custom loan terms between 1 and 40 years for fixed-rate mortgages.

## Adjustable-Rate Mortgages (ARM)

**REQ-LOAN-004**: WHERE adjustable-rate mortgage functionality is included, the system shall support an initial fixed-rate period followed by adjustable periods.

**REQ-LOAN-005**: WHERE ARM functionality is included, the system shall support common ARM configurations: 3/1, 5/1, 7/1, and 10/1 (fixed years/adjustment frequency).

**REQ-LOAN-006**: WHERE ARM functionality is included, WHEN the fixed period ends, THEN the system shall allow the interest rate to be adjusted at specified intervals.

**REQ-LOAN-007**: WHERE ARM functionality is included, the system shall support specifying rate adjustment caps (maximum rate change per adjustment period).

**REQ-LOAN-008**: WHERE ARM functionality is included, the system shall support lifetime rate caps (maximum rate over loan life).

## Principal Amount Constraints

**REQ-LOAN-009**: The system shall support principal loan amounts from $1,000 to $10,000,000.

**REQ-LOAN-010**: The system shall accept principal amounts as whole dollars or with cents.

## Interest Rate Constraints

**REQ-LOAN-011**: The system shall support annual interest rates from 0% to 20%.

**REQ-LOAN-012**: The system shall support interest rates with up to 3 decimal places of precision (e.g., 5.125%).

## Down Payment and LTV

**REQ-LOAN-013**: WHERE down payment calculation is included, the system shall calculate loan-to-value (LTV) ratio as: (principal / property value) × 100.

**REQ-LOAN-014**: WHERE down payment calculation is included, WHEN a property value and down payment are provided, THEN the system shall calculate the principal as: property value - down payment.

**REQ-LOAN-015**: WHERE down payment calculation is included, the system shall express LTV ratio as a percentage rounded to 2 decimal places.

**REQ-LOAN-016**: WHERE down payment calculation is included, the system shall support down payments expressed as a dollar amount or as a percentage of property value.
