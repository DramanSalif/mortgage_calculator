import numpy as np


class MortgageCalculator:
    # Create a class variable
    logic_count = 0
    # To create the mortgage calculation logic, input a loan principal, a periodic interest rate, the number of payments per year. the total number of payments,  a regular payment amount, and some aAdditional costs (local and state taxes, insurance) 

    def __init__(self, principal, annual_rate, years, payments_per_year, property_tax_rate, insurance_rate):
        """Initialize the mortgage calculator with a loan principal, a periodic interest rate, the number 
        of payments per year. the total number of payments,  a regular payment amount, and some additional 
        costs (local and state taxes, insurance)"""
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.payments_per_year = payments_per_year
        self.total_payments = years * payments_per_year
        self.property_tax_rate = property_tax_rate
        self.insurance_rate = insurance_rate
        # Assign an `id` to the calculation logic when it is constructed by incrementing the counter and assigning the value to `id`
        MortgageCalculator.logic_count += 1
        self.id = MortgageCalculator.logic_count
        

    def __repr__(self):
        # Printing a mortgage calculation logic will tell you its loan principal, its annual interest rate, its number of years, the total number of payments,  a regular payment amount, and some additional costs (local and state taxes, insurance
        return "This mortgage calculation logic includes {annual_rate} of annual interest rate,  {property_tax_rate} of property taxes rate, {insurance_rate} of insurance rate, {payments_per_year} payments per year over {years} years lifetime based on {principal} principal loan user-provided input.".format(principal = self.principal, annual_rate = self.annual_rate, years = self.years, payments_per_year = self.payments_per_year, property_tax_rate = self.property_tax_rate, insurance_rate = self.insurance_rate)  


    def calculate_monthly_payment(self):
        r = self.annual_rate / (100 * self.payments_per_year) # monthly interest rate
        P = self.principal                                    # principal loan amount
        n = self.total_payments                               # number of payments

        monthly_payment = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return monthly_payment

    def calculate_total_interest(self, monthly_payment):
        total_paid = monthly_payment * self.total_payments
        total_interest = total_paid - self.principal
        return total_interest

    def calculate_additional_costs(self):
        property_tax = (self.principal * self.property_tax_rate) / 100 / self.payments_per_year
        insurance = (self.principal * self.insurance_rate) / 100 / self.payments_per_year
        return property_tax + insurance

    def total_monthly_payment(self):
        monthly_payment = self.calculate_monthly_payment()
        additional_costs = self.calculate_additional_costs()
        return monthly_payment + additional_costs
# Testing
# print(MortgageCalculator(300000.00, 0.035, 30, 12, 0.0125, 0.005))
print("Welcome to the Mortgage Calculator!")
    
    # User Input
try:
    principal = float(input("Enter the loan principal amount: "))
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
years = int(input("Enter the loan term (in years): "))
payments_per_year = int(input("Enter the number of payments per year: "))
property_tax_rate = float(input("Enter the annual property tax rate (as a percentage): "))
insurance_rate = float(input("Enter the annual insurance rate (as a percentage): "))
    
# Create MortgageCalculator instance
calculator = MortgageCalculator(principal, annual_rate, years, payments_per_year, property_tax_rate, insurance_rate)
    
# Calculate results
monthly_payment = calculator.total_monthly_payment()
total_interest = calculator.calculate_total_interest(calculator.calculate_monthly_payment())
    
# Output results
print(f"\nTotal Monthly Payment (including taxes and insurance): ${monthly_payment:.2f}")
print(f"Total Interest Paid over the Life of the Loan: ${total_interest:.2f}")