# load the necessary libraries
import csv

# Function to add an expense
def add_expense(expenses):
    user_expense = input("Enter Expense name: ")

    # Validate the user input for amount
    try:
        user_amount = float(input("Enter an amount: "))

    # Handle invalid input for amount
    except ValueError:
        print("INVALID INPUT. Please enter a valid amount.")
        return

    if user_amount <= 0:
        print("INVALID INPUT. Please enter a postive amount.")
        return

    # Create a dictionary for the expense and append it to the expenses list
    expense = {"name": user_expense, "amount": user_amount}
    expenses.append(expense)
    save_changes(expenses)
    

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
                expense = {"name": row["name"], "amount": float(row["amount"])}
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

  