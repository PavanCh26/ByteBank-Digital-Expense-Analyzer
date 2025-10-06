from data_handler import load_expenses, export_to_csv
from expense_manager import add_expense, view_expenses, update_expense, delete_expense, filter_expenses
from report_generator import total_expenses, category_report, summary_dashboard

def main():
    expenses = load_expenses()
    while True:
        print("\nByteBank - Digital Expense Analyzer")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Filter Expenses")
        print("6. Total Expenses")
        print("7. Category Report")
        print("8. Summary Dashboard")
        print("9. Export to CSV")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            update_expense(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            filter_expenses(expenses)
        elif choice == '6':
            total_expenses(expenses)
        elif choice == '7':
            category_report(expenses)
        elif choice == '8':
            summary_dashboard(expenses)
        elif choice == '9':
            export_to_csv(expenses)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
