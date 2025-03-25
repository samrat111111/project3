import csv

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter description: ")
        category = input("Enter category (Food, Transport, Entertainment, etc.): ")
        
        with open("expenses.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, description, category])
        
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value for amount.\n")

# Function to view expense summary
def view_summary():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        
        if not expenses:
            print("No expenses recorded yet.\n")
            return
        
        total_expense = 0
        category_summary = {}
        
        print("Expense Summary:")
        for amount, description, category in expenses:
            amount = float(amount)
            total_expense += amount
            category_summary[category] = category_summary.get(category, 0) + amount
        
        print(f"Total Expenses: ${total_expense:.2f}")
        print("Category-wise Breakdown:")
        for cat, amt in category_summary.items():
            print(f"{cat}: ${amt:.2f}")
        print("")
    except FileNotFoundError:
        print("No expense data found. Add an expense first.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

# Main loop
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()