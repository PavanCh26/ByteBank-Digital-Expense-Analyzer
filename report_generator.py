def total_expenses(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: ${total:.2f}")

def category_report(expenses):
    report = {}
    for exp in expenses:
        report[exp['category']] = report.get(exp['category'], 0) + exp['amount']
    print("Expenses by category:")
    for cat, amt in report.items():
        print(f"{cat}: ${amt:.2f}")

def summary_dashboard(expenses):
    if not expenses:
        print("No expenses found.")
        return
    amounts = [exp['amount'] for exp in expenses]
    print(f"Total: ${sum(amounts):.2f}")
    print(f"Maximum: ${max(amounts):.2f}")
    print(f"Minimum: ${min(amounts):.2f}")
    print(f"Average: ${sum(amounts)/len(amounts):.2f}")
  
