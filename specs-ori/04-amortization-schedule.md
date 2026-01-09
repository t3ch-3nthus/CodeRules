# Amortization Schedule Specifications

## Schedule Generation

**REQ-AMORT-001**: The system shall generate an amortization schedule showing the breakdown of each payment over the life of the loan.

**REQ-AMORT-002**: WHEN generating an amortization schedule, THEN the system shall include the following information for each payment: payment number, payment date, payment amount, principal portion, interest portion, and remaining balance.

**REQ-AMORT-003**: The system shall calculate the remaining balance after each payment as: previous balance - principal portion of current payment.

**REQ-AMORT-004**: The system shall ensure the remaining balance after the final payment equals $0.00 or has a difference less than $0.01 due to rounding.

## Payment Dates

**REQ-AMORT-005**: WHEN a loan start date is provided, THEN the system shall calculate payment dates as monthly intervals from the start date.

**REQ-AMORT-006**: WHEN calculating monthly payment dates, IF a payment date falls on a day that doesn't exist in a month (e.g., February 30), THEN the system shall use the last day of that month.

**REQ-AMORT-007**: The system shall use the first day of the following month as the first payment date if no specific start date is provided.

## Schedule Formats

**REQ-AMORT-008**: The system shall support generating amortization schedules in monthly payment intervals.

**REQ-AMORT-009**: WHERE annual summary is included, the system shall support generating annual summaries showing total principal and interest paid per year.

**REQ-AMORT-010**: The system shall number payments sequentially starting from 1.

## Running Totals

**REQ-AMORT-011**: WHERE running totals are included, the system shall track cumulative principal paid up to each payment.

**REQ-AMORT-012**: WHERE running totals are included, the system shall track cumulative interest paid up to each payment.

**REQ-AMORT-013**: WHERE running totals are included, the system shall display the cumulative amounts in the amortization schedule.

## Rounding and Precision

**REQ-AMORT-014**: The system shall round all monetary values in the amortization schedule to 2 decimal places.

**REQ-AMORT-015**: WHEN rounding causes the final payment to differ from the calculated monthly payment, THEN the system shall adjust the final payment to pay off the exact remaining balance.

**REQ-AMORT-016**: The system shall ensure that the sum of all principal portions equals the original principal amount within $0.01.

## Extra Payments Impact

**REQ-AMORT-017**: WHERE extra payment functionality is included, WHEN an extra payment is made, THEN the system shall recalculate the amortization schedule from that point forward.

**REQ-AMORT-018**: WHERE extra payment functionality is included, WHEN an extra payment is applied, THEN the system shall reduce the remaining balance and either shorten the loan term or reduce subsequent payment amounts based on user preference.

**REQ-AMORT-019**: WHERE extra payment functionality is included, the system shall clearly indicate in the schedule which payments include extra amounts.

**REQ-AMORT-020**: WHERE extra payment functionality is included, the system shall calculate the time saved and interest saved due to extra payments.
