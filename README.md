# Expense Tracker

A simple command-line expense tracker built with Python. The program allows users to add expenses, view saved expenses, and calculate total spending. Expenses are stored in a CSV file so they persist between program sessions.

## Features

* Add new expenses
* View saved expenses
* Calculate total expenses
* Save expenses to a CSV file
* Load previously saved expenses when the program starts
* Handle invalid amount input without crashing

## How It Works

When the program starts, `load_expenses()` reads existing expenses from `expenses.csv`. If the file does not exist, the program starts with an empty expense list.

When a new expense is added, `save_changes()` writes the updated expense list to the CSV file.

## How to Run

Make sure Python 3 is installed, then run the program from the project directory:

```bash
python3 tracker.py
```

Follow the menu prompts to add, view, or calculate expenses.

## Technologies

* Python 3
* CSV
* Git/GitHub
