

# Expense Tracker - Final Python Project
# InternNova Week 6 Assignment

import csv
import datetime
import os

FILE_NAME = "expenses.csv"

class Expense:
    def __init__(self, category, description, amount, date=None):
        self.category = category
        self.description = description
        self.__amount = float(amount)
        self.date = date or str(datetime.date.today())

    def get_amount(self):
        return self.__amount

    def display(self):
        print(
            f"Date: {self.date} | "
            f"Category: {self.category} | "
            f"Description: {self.description} | "
            f"Amount: Rs. {self.__amount:.2f}"
        )

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    expense = Expense(
                        row["category"],
                        row["description"],
                        row["amount"],
                        row["date"]
                    )
                    self.expenses.append(expense)

        except (OSError, ValueError, KeyError, csv.Error):
            print("Warning: Could not load some expense data.")

    def save_expenses(self):
        try:
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
                fieldnames = [
                    "date",
                    "category",
                    "description",
                    "amount"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for expense in self.expenses:
                    writer.writerow({
                        "date": expense.date,
                        "category": expense.category,
                        "description": expense.description,
                        "amount": expense.get_amount()
                    })

            return True

        except OSError:
            print("Error: Unable to save expense records.")
            return False

    def add_expense(self):
        print("\n--- Add Expense ---")

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if not category or not description:
            print("Error: Category and description cannot be empty.")
            return

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                return

            expense = Expense(category, description, amount)
            self.expenses.append(expense)

            if self.save_expenses():
                print("Expense added successfully!")
            else:
                self.expenses.pop()

        except ValueError:
            print("Error: Please enter a valid numeric amount.")

    def view_expenses(self):
        print("\n--- All Expenses ---")

        if not self.expenses:
            print("No expenses found.")
            return

        for index, expense in enumerate(self.expenses, start=1):
            print(f"\nExpense {index}:")
            expense.display()

    def calculate_total(self):
        total = sum(
            expense.get_amount()
            for expense in self.expenses
        )

        print(f"\nTotal Expenses: Rs. {total:.2f}")

    def run(self):
        while True:
            print("\n==============================")
            print("       EXPENSE TRACKER")
            print("==============================")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Calculate Total")
            print("4. Exit")
            print("==============================")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.calculate_total()

            elif choice == "4":
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice. Please select 1 to 4.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()