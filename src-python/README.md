# Mortgage Calculator - Python Implementation

This is a comprehensive mortgage calculator implementation based on EARS (Easy Approach to Requirements Syntax) specifications.

## Features

Implements 171 requirements across the following categories:
- Core mortgage calculations (monthly payment, interest, amortization)
- Input validation with detailed error messages
- Loan types and parameters (fixed-rate mortgages, LTV calculation)
- Amortization schedule generation
- Additional features (property tax, insurance, PMI, HOA, extra payments)
- Comprehensive output and reporting
- Edge case handling

## Installation

1. Install Python 3.7 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the mortgage calculator with the default input file:

```bash
python mortgage_app.py
```

This reads from `input/loan_params.json` and generates reports in the `output/` directory.

### Custom Input File

Specify a custom input file:

```bash
python mortgage_app.py input/loan_params_full_features.json
```

### Input File Format

Create a JSON file with the following structure:

```json
{
  "principal": 300000,
  "annual_interest_rate": 4.5,
  "loan_term_years": 30,
  "start_date": "2024-01-01",
  "property_value": null,
  "down_payment": null,
  "annual_property_tax": null,
  "annual_insurance": null,
  "pmi_rate": null,
  "monthly_hoa": null,
  "extra_monthly_payment": null
}
```

#### Required Parameters:
- `principal`: Loan amount ($1,000 to $10,000,000)
- `annual_interest_rate`: Annual interest rate as percentage (0% to 20%)
- `loan_term_years`: Loan term in years (1 to 40)

#### Optional Parameters:
- `start_date`: Loan start date (YYYY-MM-DD format, defaults to first of next month)
- `property_value`: Property value for LTV calculation
- `down_payment`: Down payment amount
- `annual_property_tax`: Annual property tax amount
- `annual_insurance`: Annual homeowners insurance premium
- `pmi_rate`: PMI rate as percentage (0.1% to 2.0%, applied if LTV > 80%)
- `monthly_hoa`: Monthly HOA fees
- `extra_monthly_payment`: Recurring extra monthly principal payment

Set optional parameters to `null` if not needed.

## Output Files

The application generates the following output files in the `output/` directory:

1. **loan_summary.txt**: Complete loan summary with key metrics and breakdowns
2. **amortization_schedule.txt**: Full amortization schedule table
3. **amortization_schedule.csv**: CSV export of amortization schedule
4. **annual_summary.txt**: Year-by-year summary of principal and interest
5. **calculation_results.json**: Complete results in JSON format for programmatic access

## Module Structure

- `mortgage_app.py`: Main application entry point
- `calculator.py`: Core mortgage calculations (REQ-CALC series)
- `validator.py`: Input validation (REQ-VAL series)
- `amortization.py`: Amortization schedule generation (REQ-AMORT series)
- `features.py`: Additional features like PMI, taxes, insurance (REQ-FEAT and REQ-LOAN series)
- `output.py`: Output formatting and reporting (REQ-OUT series)

## Requirements Traceability

Each module and function includes comments referencing the specific EARS requirements it implements (e.g., `REQ-CALC-001`, `REQ-VAL-015`). This enables bidirectional traceability between code and specifications.

## Example Scenarios

### Basic Fixed-Rate Mortgage
See `input/loan_params.json` for a simple 30-year fixed-rate mortgage.

### Full-Featured Scenario
See `input/loan_params_full_features.json` for a scenario including:
- Property tax and insurance
- PMI (due to LTV > 80%)
- HOA fees
- Extra monthly payments

## Error Handling

The application validates all inputs according to the EARS specifications and provides clear, actionable error messages if validation fails. All validation errors are reported at once (not just the first error).

## Edge Cases

The implementation handles numerous edge cases including:
- Zero interest rate loans
- Very short (1 year) and very long (40 year) terms
- Fractional year terms (e.g., 15.5 years)
- Rounding and precision issues
- Date handling (e.g., loans starting on Jan 31st)
- PMI removal when LTV drops to 80%
- Extra payments exceeding remaining balance

## Notes

- All monetary values are rounded to 2 decimal places
- Interest rates support up to 3 decimal places
- The final loan balance is guaranteed to be $0.00 (within $0.01 tolerance)
- Dates use ISO 8601 format (YYYY-MM-DD)
