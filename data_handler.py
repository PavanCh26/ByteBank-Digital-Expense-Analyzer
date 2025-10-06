import json
import csv

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def export_to_csv(expenses, filename="expenses_report.csv"):
    if not expenses:
        print("No expenses to export.")
        return
    keys = expenses[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses exported to {filename} successfully!")
