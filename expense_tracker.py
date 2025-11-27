import json
import os
from datetime import date

# Constants
FILE_NAME = "expenses.json"

def load_data():
    """
    Requirement 3: Data Persistence.
    Loads expenses from the file at startup so data persists between runs.
    """
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return [] # Return empty list if file is corrupt or empty
    return []

def save_data(expenses):
    """
    Requirement 3: Data Persistence.
    Saves the current list of expenses to a JSON file.
    """
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(expenses, file, indent=4)
        print("Data saved successfully.")
    except IOError:
        print("Error: Could not save data to file.")

def add_expense(expenses):
    """
    Requirement 1: Add Expense.
    Allows users to log amount, category, and date.
    """
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (e.g., Food, Transport): ").strip().title()
        
        # We automatically use today's date for simplicity, 
        # but you could allow user input here if preferred.
        expense_date = str(date.today())
        
        # Store as a dictionary [Requirement 1]
        expense = {
            "amount": amount,
            "category": category,
            "date": expense_date
        }
        expenses.append(expense)
        print(f"Expense of ${amount} added for {category} on {expense_date}.")
        
    except ValueError:
        print("Invalid input! Please enter a numeric value for the amount.")

def view_summary(expenses):
    """
    Requirement 2: View Summary.
    Displays total spending per category, overall total, and a daily log.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total_overall = 0
    category_totals = {}

    print("\n" + "="*40)
    print("EXPENSE SUMMARY")
    print("="*40)

    # Calculate totals
    for item in expenses:
        amt = item['amount']
        cat = item['category']
        
        # Add to overall total
        total_overall += amt
        
        # Add to category total
        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt

    # 1. Total spending by category
    print(f"{'Category':<20} | {'Amount':<10}")
    print("-" * 35)
    for cat, amount in category_totals.items():
        print(f"{cat:<20} | ${amount:<10.2f}")
    
    # 2. Total overall spending
    print("-" * 35)
    print(f"{'TOTAL SPENDING':<20} | ${total_overall:<10.2f}")
    print("="*40)
    
    # 3. Spending over time (Simple daily log)
    print("\n--- History (Spending over Time) ---")
    for item in expenses:
        print(f"{item['date']}: ${item['amount']} - {item['category']}")

def main():
    """
    Requirement 4: User Menu.
    Main loop handling user choices.
    """
    expenses = load_data() # Load data on start [Requirement 3]
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add an Expense")
        print("2. View Summaries")
        print("3. Save & Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            save_data(expenses)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()