# Edge Cases and Special Scenarios Specifications

## Zero Interest Rate

**REQ-EDGE-001**: WHEN the interest rate is exactly 0%, THEN the system shall calculate monthly payment as: principal / number of months.

**REQ-EDGE-002**: WHEN the interest rate is 0%, THEN the total interest paid shall be $0.00.

**REQ-EDGE-003**: WHEN the interest rate is 0%, THEN each payment shall be entirely principal with $0.00 interest portion.

## Very Small Principal Amounts

**REQ-EDGE-004**: WHEN the principal amount is at the minimum threshold ($1,000), THEN the system shall perform calculations accurately without errors.

**REQ-EDGE-005**: IF the monthly payment would be less than $1.00, THEN the system shall still calculate and display the accurate payment amount.

## Very Large Principal Amounts

**REQ-EDGE-006**: WHEN the principal amount is at the maximum threshold ($10,000,000), THEN the system shall perform calculations accurately without overflow errors.

**REQ-EDGE-007**: The system shall maintain precision for calculations involving principal amounts up to $10,000,000.

## Very Short Loan Terms

**REQ-EDGE-008**: WHEN the loan term is 1 year (12 payments), THEN the system shall generate an accurate 12-payment amortization schedule.

**REQ-EDGE-009**: WHEN the loan term is less than 1 month, THEN the system shall handle the calculation appropriately or reject with a clear error message.

## Very Long Loan Terms

**REQ-EDGE-010**: WHEN the loan term is 40 years (480 payments), THEN the system shall generate an accurate 480-payment amortization schedule.

**REQ-EDGE-011**: WHEN the loan term is 40 years, THEN the system shall accurately calculate total interest even when it significantly exceeds the principal.

## Fractional Year Terms

**REQ-EDGE-012**: WHEN the loan term includes fractional years (e.g., 15.5 years), THEN the system shall convert it to the correct number of months (186 months).

**REQ-EDGE-013**: WHEN the loan term in months is not a whole number, THEN the system shall round to the nearest whole month.

## Very Low Interest Rates

**REQ-EDGE-014**: WHEN the interest rate is very low (e.g., 0.001%), THEN the system shall maintain calculation precision and not round to zero prematurely.

**REQ-EDGE-015**: WHEN the interest rate is very low, THEN the system shall ensure the monthly payment is greater than the monthly interest to avoid infinite loan terms.

## Very High Interest Rates

**REQ-EDGE-016**: WHEN the interest rate is at the maximum threshold (20%), THEN the system shall calculate payments accurately.

**REQ-EDGE-017**: WHEN the interest rate is high, THEN the system shall handle cases where total interest significantly exceeds principal.

## Rounding Edge Cases

**REQ-EDGE-018**: WHEN rounding causes the sum of principal portions to not equal exactly the original principal, THEN the system shall adjust the final payment to ensure the loan is fully paid.

**REQ-EDGE-019**: WHEN the final payment would be less than $0.01, THEN the system shall combine it with the previous payment.

**REQ-EDGE-020**: The system shall ensure no payment has a negative principal or interest portion due to rounding errors.

## Extra Payment Edge Cases

**REQ-EDGE-021**: WHERE extra payment functionality is included, WHEN an extra payment equals exactly the remaining balance, THEN the system shall mark the loan as paid off.

**REQ-EDGE-022**: WHERE extra payment functionality is included, WHEN an extra payment exceeds the remaining balance, THEN the system shall only apply the amount needed and indicate the excess.

**REQ-EDGE-023**: WHERE extra payment functionality is included, WHEN an extra payment is made on the first payment, THEN the system shall recalculate the entire amortization schedule.

**REQ-EDGE-024**: WHERE extra payment functionality is included, WHEN an extra payment is made on the last payment, THEN the system shall apply it correctly and potentially pay off the loan early.

## PMI Edge Cases

**REQ-EDGE-025**: WHERE PMI calculation is included, WHEN the LTV is exactly 80%, THEN PMI shall not be applied.

**REQ-EDGE-026**: WHERE PMI calculation is included, WHEN the LTV drops to exactly 80% mid-loan, THEN PMI shall be removed starting with the next payment.

**REQ-EDGE-027**: WHERE PMI calculation is included, IF the remaining balance equals exactly 80% of original property value due to rounding, THEN the system shall remove PMI.

## Date Handling Edge Cases

**REQ-EDGE-028**: WHEN a loan starts on January 31st, THEN February payment shall be on February 28th (or 29th in leap years).

**REQ-EDGE-029**: WHEN a loan starts on the 29th, 30th, or 31st, THEN the system shall consistently handle months with fewer days.

**REQ-EDGE-030**: WHEN calculating payment dates, THEN the system shall correctly handle leap years.

## Boundary Value Cases

**REQ-EDGE-031**: The system shall correctly handle the boundary values for all input parameters (minimum and maximum values).

**REQ-EDGE-032**: IF an input is exactly at a boundary value, THEN the system shall accept it as valid.

**REQ-EDGE-033**: IF an input is one cent or one basis point outside the acceptable range, THEN the system shall reject it.

## Precision and Accuracy

**REQ-EDGE-034**: The system shall maintain at least 2 decimal places of precision throughout all internal calculations before final rounding.

**REQ-EDGE-035**: WHEN performing intermediate calculations, THEN the system shall not round until the final output stage to minimize cumulative rounding errors.

**REQ-EDGE-036**: The system shall ensure that mathematical identities hold within acceptable rounding tolerances (e.g., monthly payment × number of payments ≈ total amount paid).

## Concurrent Calculations

**REQ-EDGE-037**: WHEN multiple calculations are performed with the same inputs, THEN the system shall produce identical results.

**REQ-EDGE-038**: The system shall not have race conditions or state management issues that could cause calculation inconsistencies.
