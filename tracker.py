# load the necessary libraries
import csv
import math

# Function to add an expense
def add_expense(expenses):

    while True:
        user_expense = input("Enter Expense name: ").strip()
        
        if user_expense:
            print(f"Expense name '{user_expense}' is valid.")
            break

        else:
            print("Invalid input. Please enter a valid expense name.")


    # Validate the user input for amount
    while True:
        try:
            user_amount = float(input("Enter an amount: "))

            if not math.isfinite(user_amount) or user_amount <= 0:
                print("Invalid input. Please enter a positive amount.")
                continue
        
            break

        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

    
    # Create a dictionary for the expense and append it to the expenses list
    expense = {"name": user_expense, "amount": user_amount}
    expenses.append(expense)
    save_changes(expenses)
    
    print(f"Expense '{user_expense}' of amount {user_amount} added successfully.")
    

# Function to view expenses
def view_expenses(expenses):
    for expense in expenses:
        print(f"Expense: {expense['name']}, Amount: {expense['amount']}")



# Function to calculate the total expenses
def calculate_total(expenses):
    total = 0 

# Iterate through the expenses and sum up the amounts
    for expense in expenses:
        total+=expense['amount']
    return total


# Function to load expenses from a CSV file
def load_expenses():
    expenses = []

    # Try to open the expenses.csv file and read its contents
    try:
        with open('expenses.csv','r') as file:
            reader = csv.DictReader(file)

    # Iterate through each row in the CSV file and create a dictionary for each expense
            for row in reader:
                try:
                    amount = float(row['amount'])

                    if not math.isfinite(amount) or amount <= 0:
                        print(f"Skipping expense with invalid amount: {row['amount']}")
                        continue
                except (ValueError, TypeError):
                    print(f"Skipping expense with invalid amount: {row['amount']}")
                    continue

                name = row['name'].strip()


                if not name:
                    print("Skipping expense with empty name.")
                    continue

                expense = {"name": name, "amount": amount}
                expenses.append(expense)

        return expenses
    
    # Handle the case where the expenses.csv file does not exist
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")
        return expenses

# Function to save changes to the expenses list back to the CSV file
def save_changes(expenses):

    # Save the expenses to a CSV file
    with open('expenses.csv', 'w', newline ='') as file:

    # Create a CSV DictWriter object to write the expenses to the file
        writer = csv.DictWriter(file, fieldnames = ['name', 'amount'])
        writer.writeheader()
        writer.writerows(expenses)




# Main program loop
expenses = load_expenses()

# Display the menu and handle user choices
while True:
    print("1 - Add Expense")
    print("2 - View Expenses")
    print("3 - Calculate Total Expenses")
    print("4 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        total = calculate_total(expenses)
        print(f"Total Expenses: {total}")
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

  