import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
from datetime import datetime

# Function to log an expense
def log_expense():
    name = input("Enter your name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    amount = float(input("Enter the amount spent: "))
    
    with open("expenses.csv", "a", newline="") as csvfile:
        fieldnames = ['Name', 'Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Date': date, 'Description': description, 'Amount': amount})
    print("Expense logged successfully.")

# Function to analyze expenses
def analyze_expenses():
    try:
        df = pd.read_csv("expenses.csv")
        total_expenses = df.groupby('Name')['Amount'].sum()
        average_daily_expense = total_expenses.sum() / len(df['Date'].unique())
        
        print("Total Expenses by Family Member:")
        print(total_expenses)
        print(f"Average Daily Expense for the Household: {average_daily_expense:.2f}")
    except FileNotFoundError:
        print("No expenses found. Please log expenses first.")

# Function to generate an expense trend chart
def generate_expense_chart():
    try:
        df = pd.read_csv("expenses.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        
        daily_expenses = df.groupby(pd.Grouper(freq='D'))['Amount'].sum()
        cumulative_expenses = daily_expenses.cumsum()
        
        plt.figure(figsize=(10, 5))
        plt.plot(cumulative_expenses.index, cumulative_expenses.values)
        plt.xlabel("Date")
        plt.ylabel("Cumulative Expenses")
        plt.title("Expense Trends Over the Last Month")
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("No expenses found. Please log expenses first.")

# Main loop for user interaction
while True:
    print("\nHousehold Expenses Tracker Menu:")
    print("1. Log an Expense")
    print("2. Analyze Expenses")
    print("3. Generate Expense Chart")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        log_expense()
    elif choice == "2":
        analyze_expenses()
    elif choice == "3":
        generate_expense_chart()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
