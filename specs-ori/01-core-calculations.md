# Core Mortgage Calculations Specifications

## Monthly Payment Calculation

**REQ-CALC-001**: The system shall calculate the monthly mortgage payment using the formula: M = P[r(1+r)^n]/[(1+r)^n-1] where M is monthly payment, P is principal loan amount, r is monthly interest rate, and n is number of monthly payments.

**REQ-CALC-002**: WHEN the user provides a principal amount, annual interest rate, and loan term in years, THEN the system shall convert the annual interest rate to a monthly rate by dividing by 12.

**REQ-CALC-003**: WHEN the user provides a loan term in years, THEN the system shall convert it to the number of monthly payments by multiplying by 12.

**REQ-CALC-004**: IF the annual interest rate is 0%, THEN the system shall calculate the monthly payment as principal divided by number of months.

**REQ-CALC-005**: The system shall express the monthly payment result rounded to 2 decimal places.

## Total Interest Calculation

**REQ-CALC-006**: The system shall calculate the total interest paid over the life of the loan as: (monthly payment × number of payments) - principal amount.

**REQ-CALC-007**: The system shall calculate the total amount paid as: monthly payment × number of payments.

**REQ-CALC-008**: The system shall express total interest and total amount paid rounded to 2 decimal places.

## Interest Rate Conversions

**REQ-CALC-009**: WHEN an annual percentage rate (APR) is provided, THEN the system shall convert it to a decimal by dividing by 100 before calculations.

**REQ-CALC-010**: The system shall support interest rates expressed as percentages (e.g., 5.5%) or decimals (e.g., 0.055).

## Principal and Interest Breakdown

**REQ-CALC-011**: The system shall calculate the interest portion of any payment as: remaining balance × monthly interest rate.

**REQ-CALC-012**: The system shall calculate the principal portion of any payment as: monthly payment - interest portion.

**REQ-CALC-013**: WHEN calculating payment breakdowns, THEN the system shall ensure the principal portion does not exceed the remaining balance.
