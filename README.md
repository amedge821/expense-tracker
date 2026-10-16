# Expense Tracker

A command-line expense tracker built with Python that allows users to record expenses, view saved expenses, and calculate total spending. Expenses are stored in a CSV file so they persist between program sessions.

## Features

- **Add expenses:** Enter an expense name and amount.
- **Input validation:** Rejects empty expense names, non-numeric amounts, and zero or negative amounts.
- **View expenses:** Display recorded expenses.
- **Calculate total spending:** Calculate the total amount of recorded expenses.
- **CSV persistence:** Save expenses to `expenses.csv` and load them when the program starts.
- **Error handling:** Handles missing CSV files and skips rows with invalid expense data.

## Requirements

- Python 3
- No external libraries required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/amedge821/expense-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd expense-tracker
   ```

3. Run the program:

   ```bash
   python3 tracker.py
   ```

## Usage

Follow the command-line menu:

1. Add Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit

Enter the corresponding number to select an option. When adding an expense, provide a name and a positive numeric amount.

## Data Storage

Expenses are stored locally in `expenses.csv`. Previously saved expenses are loaded when the program starts, allowing records to persist between sessions.

## Technologies

- Python
- CSV file handling
- Exception handling
- Input validation
- Command-line interfaces

## Future Improvements

- Add expense categories.
- Filter expenses by category or date.
- Generate monthly spending summaries.
- Add automated unit tests.
