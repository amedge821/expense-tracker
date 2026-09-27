import csv

def add_expense(expenses):
    user_expense = input("Enter Expense name: ")

    try:
        user_amount = float(input("Enter an amount: "))
    except ValueError:
        print("INVALID INPUT. Please enter a valid amount.")
        return

    expense = {"name": user_expense, "amount": user_amount}
    expenses.append(expense)
    save_changes(expenses)
    

def view_expenses(expenses):
    for expense in expenses:
        print(f"Expense: {expense['name']}, Amount: {expense['amount']}")



def calculate_total(expenses):
    total = 0 

    for expense in expenses:
        total+=expense['amount']
    return total


def load_expenses():
    expenses = []
    try:
        with open('expenses.csv','r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = {"name": row["name"], "amount": float(row["amount"])}
                expenses.append(expense)
            return expenses

    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")
        return expenses

def save_changes(expenses):

    with open('expenses.csv', 'w', newline ='') as file:
        writer = csv.DictWriter(file, fieldnames = ['name', 'amount'])
        writer.writeheader()
        writer.writerows(expenses)





expenses = load_expenses()

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

  