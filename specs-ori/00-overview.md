# Mortgage Calculator - EARS Specifications Overview

## Purpose

This document provides an overview of the EARS (Easy Approach to Requirements Syntax) specifications for a comprehensive mortgage calculator system. These specifications are designed to support a benchmark for:

1. Code generation from specifications
2. Bidirectional traceability between specifications and code
3. Specification extraction from code
4. Validation of completeness (no left-behind elements)
5. Detection of artificial or hallucinated requirements

## Specification Structure

The specifications are organized into the following modules:

### 01-core-calculations.md
Core mortgage calculation algorithms including monthly payment, total interest, and principal/interest breakdown.
- **Requirements**: REQ-CALC-001 through REQ-CALC-013
- **Count**: 13 requirements

### 02-loan-types-parameters.md
Specifications for different loan types (fixed-rate, ARM) and parameter constraints.
- **Requirements**: REQ-LOAN-001 through REQ-LOAN-016
- **Count**: 16 requirements

### 03-input-validation.md
Input validation rules and error handling for all user inputs.
- **Requirements**: REQ-VAL-001 through REQ-VAL-021
- **Count**: 21 requirements

### 04-amortization-schedule.md
Amortization schedule generation, formatting, and calculations.
- **Requirements**: REQ-AMORT-001 through REQ-AMORT-020
- **Count**: 20 requirements

### 05-additional-features.md
Optional features including property tax, insurance, PMI, HOA fees, extra payments, and refinance analysis.
- **Requirements**: REQ-FEAT-001 through REQ-FEAT-031
- **Count**: 31 requirements

### 06-output-reporting.md
Output formatting, reporting, visualization, and user messaging.
- **Requirements**: REQ-OUT-001 through REQ-OUT-032
- **Count**: 32 requirements

### 07-edge-cases-special-scenarios.md
Edge cases, boundary conditions, and special scenarios.
- **Requirements**: REQ-EDGE-001 through REQ-EDGE-038
- **Count**: 38 requirements

## Total Requirements Count

**Total**: 171 individual requirements

## EARS Pattern Distribution

The specifications use the following EARS patterns:

1. **Ubiquitous**: "The system shall..." - For universal requirements
2. **Event-driven**: "WHEN [trigger] THEN the system shall..." - For event responses
3. **State-driven**: "WHILE [state] the system shall..." - For state-dependent behavior
4. **Unwanted behavior**: "IF [condition] THEN the system shall..." - For handling specific conditions
5. **Optional**: "WHERE [feature] is included, the system shall..." - For optional features

## Requirement Naming Convention

Requirements follow the pattern: **REQ-[MODULE]-[NUMBER]**

- **CALC**: Core calculations
- **LOAN**: Loan types and parameters
- **VAL**: Input validation
- **AMORT**: Amortization schedule
- **FEAT**: Additional features
- **OUT**: Output and reporting
- **EDGE**: Edge cases and special scenarios

## Core vs. Optional Features

### Core Features (Mandatory)
- Basic monthly payment calculation
- Total interest calculation
- Fixed-rate mortgages
- Input validation
- Basic amortization schedule
- Summary output

### Optional Features (WHERE clause)
- Adjustable-rate mortgages (ARM)
- Down payment and LTV calculation
- Property tax and insurance
- Private Mortgage Insurance (PMI)
- HOA fees
- Extra payment functionality
- Early payoff calculation
- Comparison scenarios
- Refinance analysis
- Annual summaries and running totals
- Graphical visualization
- PDF export
- Progress tracking
- Affordability metrics

## Key Testable Elements

Each requirement specifies testable criteria:
1. **Inputs**: What data is required
2. **Processing**: How calculations are performed
3. **Outputs**: What results are produced
4. **Constraints**: Valid ranges and boundaries
5. **Error conditions**: What triggers errors and what messages appear

## Traceability Considerations

For benchmark purposes, each requirement should be traceable to:
- **Code implementation**: Functions, methods, or modules implementing the requirement
- **Test cases**: Tests verifying the requirement
- **Documentation**: Comments or documentation referencing the requirement
- **Validation rules**: Code validating inputs or outputs per the requirement

## Completeness Validation

To validate that specification extraction is complete, verify that:
1. All 171 requirement IDs are extractable
2. All numerical constraints (ranges, thresholds) are captured
3. All formulas and calculations are identified
4. All error messages are extracted
5. All optional feature flags are recognized
6. All EARS patterns are correctly classified

## Non-Functional Considerations

While these specifications focus on functional requirements, implementations should consider:
- **Performance**: Calculations should complete in reasonable time
- **Precision**: Maintain appropriate decimal precision
- **Usability**: Clear error messages and intuitive outputs
- **Maintainability**: Clean code structure for traceability
- **Testability**: Unit testable components

## Usage in Benchmark

This specification set provides:
- **Sufficient complexity**: 171 requirements across 7 modules
- **Diverse patterns**: All EARS patterns represented
- **Realistic scope**: Practical mortgage calculator functionality
- **Clear boundaries**: Well-defined mandatory vs. optional features
- **Testable criteria**: Specific inputs, outputs, and behaviors
- **Traceability hooks**: Unique IDs and structured organization

The specifications are designed to support automated and manual analysis of:
- Specification → Code generation accuracy
- Code → Specification extraction completeness
- Bidirectional traceability integrity
- Hallucination detection (artificial requirements)
