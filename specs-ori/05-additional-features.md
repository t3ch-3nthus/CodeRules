# Additional Features Specifications

## Property Tax Calculation

**REQ-FEAT-001**: WHERE property tax calculation is included, the system shall accept annual property tax amount.

**REQ-FEAT-002**: WHERE property tax calculation is included, the system shall calculate the monthly property tax amount by dividing annual property tax by 12.

**REQ-FEAT-003**: WHERE property tax calculation is included, the system shall add monthly property tax to the base monthly mortgage payment to calculate total monthly housing payment.

**REQ-FEAT-004**: WHERE property tax calculation is included, the system shall express monthly property tax rounded to 2 decimal places.

## Homeowners Insurance

**REQ-FEAT-005**: WHERE homeowners insurance calculation is included, the system shall accept annual homeowners insurance premium.

**REQ-FEAT-006**: WHERE homeowners insurance calculation is included, the system shall calculate monthly insurance amount by dividing annual premium by 12.

**REQ-FEAT-007**: WHERE homeowners insurance calculation is included, the system shall add monthly insurance to calculate total monthly housing payment.

**REQ-FEAT-008**: WHERE homeowners insurance calculation is included, the system shall express monthly insurance rounded to 2 decimal places.

## Private Mortgage Insurance (PMI)

**REQ-FEAT-009**: WHERE PMI calculation is included, IF the loan-to-value ratio is greater than 80%, THEN the system shall calculate and include PMI in the monthly payment.

**REQ-FEAT-010**: WHERE PMI calculation is included, the system shall calculate monthly PMI as: (principal × annual PMI rate) / 12.

**REQ-FEAT-011**: WHERE PMI calculation is included, the system shall support PMI rates between 0.1% and 2.0% of the loan amount annually.

**REQ-FEAT-012**: WHERE PMI calculation is included, WHEN the remaining balance falls below 80% of the original property value, THEN the system shall automatically remove PMI from subsequent payments.

**REQ-FEAT-013**: WHERE PMI calculation is included, the system shall track the payment number at which PMI is removed.

## HOA Fees

**REQ-FEAT-014**: WHERE HOA fee calculation is included, the system shall accept monthly homeowners association fees.

**REQ-FEAT-015**: WHERE HOA fee calculation is included, the system shall add monthly HOA fees to calculate total monthly housing payment.

## Extra Principal Payments

**REQ-FEAT-016**: WHERE extra payment functionality is included, the system shall support one-time extra principal payments.

**REQ-FEAT-017**: WHERE extra payment functionality is included, the system shall support recurring monthly extra principal payments.

**REQ-FEAT-018**: WHERE extra payment functionality is included, the system shall support annual extra principal payments.

**REQ-FEAT-019**: WHERE extra payment functionality is included, WHEN extra payments are applied, THEN the system shall reduce only the principal balance, not the interest.

**REQ-FEAT-020**: WHERE extra payment functionality is included, the system shall calculate the payoff date with extra payments.

**REQ-FEAT-021**: WHERE extra payment functionality is included, the system shall calculate total interest saved due to extra payments.

## Early Payoff Calculation

**REQ-FEAT-022**: WHERE early payoff functionality is included, WHEN a target payoff date is specified, THEN the system shall calculate the required extra monthly payment to achieve payoff by that date.

**REQ-FEAT-023**: WHERE early payoff functionality is included, IF the target payoff date is before the next scheduled payment, THEN the system shall reject the input and display an error message "Target payoff date must be in the future".

**REQ-FEAT-024**: WHERE early payoff functionality is included, the system shall calculate the lump sum amount needed to pay off the loan immediately.

## Comparison Scenarios

**REQ-FEAT-025**: WHERE comparison functionality is included, the system shall support comparing two or more loan scenarios side by side.

**REQ-FEAT-026**: WHERE comparison functionality is included, WHEN comparing scenarios, THEN the system shall display differences in total interest paid, total amount paid, and monthly payment.

**REQ-FEAT-027**: WHERE comparison functionality is included, the system shall highlight which scenario has the lowest total cost.

## Refinance Analysis

**REQ-FEAT-028**: WHERE refinance analysis is included, WHEN analyzing a refinance, THEN the system shall accept the current remaining balance as the new principal.

**REQ-FEAT-029**: WHERE refinance analysis is included, the system shall accept refinance closing costs and factor them into the break-even analysis.

**REQ-FEAT-030**: WHERE refinance analysis is included, the system shall calculate the break-even point in months where refinance savings exceed closing costs.

**REQ-FEAT-031**: WHERE refinance analysis is included, the system shall compare the total interest of continuing the current loan versus refinancing.
