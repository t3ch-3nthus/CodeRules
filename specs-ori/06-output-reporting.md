# Output and Reporting Specifications

## Summary Output

**REQ-OUT-001**: The system shall display a loan summary containing: principal amount, annual interest rate, loan term, monthly payment, total amount paid, and total interest paid.

**REQ-OUT-002**: The system shall format all monetary values with a dollar sign ($) and comma separators for thousands.

**REQ-OUT-003**: The system shall format all percentage values with a percent sign (%) and appropriate decimal places.

**REQ-OUT-004**: WHEN displaying large numbers, THEN the system shall use comma separators every three digits (e.g., $1,234,567.89).

## Detailed Breakdown

**REQ-OUT-005**: WHERE detailed breakdown is included, the system shall display the first payment breakdown showing principal and interest portions.

**REQ-OUT-006**: WHERE detailed breakdown is included, the system shall display the last payment breakdown showing principal and interest portions.

**REQ-OUT-007**: WHERE detailed breakdown is included, the system shall show the percentage of each payment going to principal versus interest.

## Amortization Schedule Output

**REQ-OUT-008**: WHEN outputting an amortization schedule, THEN the system shall format it as a table with aligned columns.

**REQ-OUT-009**: WHEN outputting an amortization schedule, THEN the system shall include column headers: Payment #, Date, Payment Amount, Principal, Interest, and Balance.

**REQ-OUT-010**: The system shall allow filtering the amortization schedule by year or payment range.

**REQ-OUT-011**: The system shall support exporting the amortization schedule to CSV format.

**REQ-OUT-012**: WHERE PDF export is included, the system shall support exporting the amortization schedule to PDF format.

## Graphical Visualization

**REQ-OUT-013**: WHERE graphical output is included, the system shall generate a graph showing the principal versus interest portion over time.

**REQ-OUT-014**: WHERE graphical output is included, the system shall generate a graph showing the remaining balance over time.

**REQ-OUT-015**: WHERE graphical output is included, the system shall use different colors to distinguish between principal and interest in visualizations.

**REQ-OUT-016**: WHERE graphical output is included, the system shall provide axis labels and a legend for all graphs.

## Key Metrics Display

**REQ-OUT-017**: The system shall calculate and display the interest-to-principal ratio for the entire loan.

**REQ-OUT-018**: The system shall calculate and display the total cost of the loan as a percentage of the original principal.

**REQ-OUT-019**: WHERE affordability metrics are included, the system shall display the principal and interest payment as a dollar amount.

**REQ-OUT-020**: WHERE affordability metrics are included, the system shall display the total housing payment (including taxes, insurance, PMI, HOA) as a dollar amount.

## Progress Tracking

**REQ-OUT-021**: WHERE progress tracking is included, WHEN a current payment number is specified, THEN the system shall calculate and display the percentage of the loan paid off.

**REQ-OUT-022**: WHERE progress tracking is included, WHEN a current payment number is specified, THEN the system shall calculate and display the remaining number of payments.

**REQ-OUT-023**: WHERE progress tracking is included, WHEN a current payment number is specified, THEN the system shall display total interest paid to date and total interest remaining.

## Comparison Output

**REQ-OUT-024**: WHERE comparison functionality is included, WHEN comparing loan scenarios, THEN the system shall output results in a side-by-side table format.

**REQ-OUT-025**: WHERE comparison functionality is included, the system shall highlight the most favorable option for each comparison metric.

## Error and Warning Messages

**REQ-OUT-026**: WHEN validation errors occur, THEN the system shall display clear, actionable error messages.

**REQ-OUT-027**: IF the loan term is unusually long (greater than 30 years), THEN the system shall display a warning message "Long loan terms result in significantly higher total interest paid".

**REQ-OUT-028**: IF the interest rate is unusually high (greater than 10%), THEN the system shall display a warning message "This interest rate is higher than typical market rates".

**REQ-OUT-029**: WHERE PMI is applicable, the system shall display an informational message indicating when PMI will be removed.

## Number Formatting Consistency

**REQ-OUT-030**: The system shall consistently round all monetary values to 2 decimal places across all outputs.

**REQ-OUT-031**: The system shall consistently display percentages to 3 decimal places for interest rates and 2 decimal places for other percentages.

**REQ-OUT-032**: The system shall use consistent date formatting across all outputs (e.g., MM/DD/YYYY or YYYY-MM-DD).
