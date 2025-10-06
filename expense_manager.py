from data_handler import load_expenses, save_expenses
from datetime import datetime

def add_expense(expenses):
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date_str.strip() == "":
        date_str = datetime.today().strftime("%Y-%m-%d")
    expense = {"name": name, "category": category, "amount": amount, "date": date_str}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['name']} - {exp['category']} - ${exp['amount']} - {exp['date']}")

def update_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the number of the expense to update: ")) - 1
    if 0 <= index < len(expenses):
        exp = expenses[index]
        exp['name'] = input(f"Enter new name ({exp['name']}): ") or exp['name']
        exp['category'] = input(f"Enter new category ({exp['category']}): ") or exp['category']
        amt = input(f"Enter new amount ({exp['amount']}): ")
        exp['amount'] = float(amt) if amt else exp['amount']
        date = input(f"Enter new date ({exp['date']}): ")
        exp['date'] = date or exp['date']
        save_expenses(expenses)
        print("Expense updated successfully!")
    else:
        print("Invalid selection.")

def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        print("Expense deleted successfully!")
    else:
        print("Invalid selection.")

def filter_expenses(expenses):
    print("1. Filter by category")
    print("2. Filter by date")
    choice = input("Enter choice: ")
    if choice == '1':
        cat = input("Enter category to filter: ")
        filtered = [e for e in expenses if e['category'].lower() == cat.lower()]
    elif choice == '2':
        date = input("Enter date (YYYY-MM-DD) to filter: ")
        filtered = [e for e in expenses if e['date'] == date]
    else:
        print("Invalid choice.")
        return
    if filtered:
        for e in filtered:
            print(f"{e['name']} - {e['category']} - ${e['amount']} - {e['date']}")
    else:
        print("No matching expenses found.")
      
