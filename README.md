# Mortgage Calculator

## Overview

The Mortgage Calculator is a user-friendly Python application designed to help prospective homeowners understand their mortgage options. By allowing users to input various parameters, such as purchase price, interest rates, and loan terms, this calculator provides clear calculations for monthly mortgage payments, total interest paid, and a detailed amortization schedule.

## Features

- **User Input**: Enter details like loan principal, annual interest rate, loan term, property tax rate, and insurance rate.
- **Monthly Payment Calculation**: Automatically calculates the total monthly payment including taxes and insurance.
- **Total Interest Calculation**: Provides insight into the total interest paid over the life of the loan.
- **Amortization Schedule**: Generates an amortization schedule displaying a breakdown of each payment.
- **Visual Representation**: Uses `matplotlib` to generate graphs of principal and interest payments over time.
- **Responsive Design**: Included frontend developed using Bootstrap for better user experience.

## Technology Stack

- **Python**: The primary language for backend calculations.
- **Flask**: Web frameworks.
- **PostgreSQL**: Database for storing user information (optional for future enhancements).
- **Bootstrap**: For responsive frontend design.
- **Matplotlib**: For graphical representation of amortization and payment schedules.

## Installation

### Prerequisites

- Python 3.6 or later
- PostgreSQL (if user account features are implemented)
- Required Python packages: `numpy`, `matplotlib`, `Flask` or `Django`, depending on your choice of framework

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/DramanSalif/mortgage-calculator.git
   cd mortgage-calculator
