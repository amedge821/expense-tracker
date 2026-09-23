expenses = []

def add_expense(expenses):

    user_expense = input("Enter Expense name: ")
    user_amount = float(input("Enter an amount: "))
    expense = {"name": user_expense, "amount": user_amount}
    expenses.append(expense)

def view_expenses(expenses):
    for expense in expenses:
        print(f"Expense: {expense['name']}, Amount: {expense['amount']}")



def calculate_total(expenses):
    total = 0 

    for expense in expenses:
        total+=expense['amount']
    return total




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