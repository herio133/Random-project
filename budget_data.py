import csv
import os
from datetime import datetime

FILENAME = 'budget_data.csv'

def load_data():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                data.append(row)
    return data

def save_data(data):
    with open(FILENAME, 'w', newline='') as file:
        fieldnames = ['date', 'type', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def add_entry(data, entry_type):
    date_str = input("Enter date (YYYY-MM-DD) [default: today]: ").strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    category = input(f"Enter {entry_type} category: ")
    while True:
        try:
            amount = float(input(f"Enter {entry_type} amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    description = input("Enter a description: ")
    entry = {
        'date': date_str,
        'type': entry_type,
        'category': category,
        'amount': amount,
        'description': description
    }
    data.append(entry)
    save_data(data)
    print(f"{entry_type.capitalize()} added!\n")

def view_records(data, date_filter=None):
    filtered = data
    if date_filter:
        filtered = [e for e in data if e['date'].startswith(date_filter)]
    if not filtered:
        print("No records found.")
        return
    print("\nDate       | Type    | Category    | Amount   | Description")
    print("-"*60)
    for entry in filtered:
        print(f"{entry['date']} | {entry['type']:<7} | {entry['category']:<10} | ${entry['amount']:>7.2f} | {entry['description']}")
    print()

def view_balance(data):
    income = sum(entry['amount'] for entry in data if entry['type'] == 'income')
    expense = sum(entry['amount'] for entry in data if entry['type'] == 'expense')
    balance = income - expense
    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expense: ${expense:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")

def category_summary(data):
    summary = {}
    for entry in data:
        cat = entry['category']
        if cat not in summary:
            summary[cat] = 0
        if entry['type'] == 'income':
            summary[cat] += entry['amount']
        else:
            summary[cat] -= entry['amount']
    print("\nCategory Summary:")
    for cat, amount in summary.items():
        print(f"{cat}: ${amount:.2f}")
    print()

def main():
    data = load_data()
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Records")
        print("4. View Records by Month (YYYY-MM)")
        print("5. View Balance")
        print("6. Category Summary")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry(data, 'income')
        elif choice == '2':
            add_entry(data, 'expense')
        elif choice == '3':
            view_records(data)
        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            view_records(data, date_filter=month)
        elif choice == '5':
            view_balance(data)
        elif choice == '6':
            category_summary(data)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
