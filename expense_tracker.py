import csv
import os

expenses = []
FILE_NAME = "expenses.csv"


def show_menu():
    print()
    print("=== PYTHON EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "date": row["date"],
                "category": row["category"],
                "description": row["description"],
                "amount": float(row["amount"])
            })


def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "description", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


def add_expense():
    print()
    print("--- Add Expense ---")

    date = input("Enter date (MM/DD/YYYY): ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not date or not category or not description:
        print("Date, category, and description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: $"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully.")


def view_expenses():
    print()
    print("--- Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"${expense['amount']:.2f}"
        )


def view_total():
    print()
    print("--- Total Spending ---")

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total spending: ${total:.2f}")


def view_by_category():
    print()
    print("--- Spending by Category ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    load_expenses()

    running = True

    while running:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            view_by_category()

        elif choice == "5":
            running = False
            print("Goodbye!")

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()