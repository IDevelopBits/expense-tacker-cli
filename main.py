import argparse
import json
import calendar

from expense import Expense

# Parser for all the expense tracker commands
def create_parser():
    parser = argparse.ArgumentParser(description="expense-tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, type=str, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount spent")

    # Subcommand: delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense to delete")
    # Subcommand: list
    subparsers.add_parser("list", help="List all expenses")
    # Subcommand: summary
    summary_parser = subparsers.add_parser("summary", help="Summary of all expenses")
    summary_parser.add_argument("--month", required=False, type=int, help="Expense for a certain month of the same year")

    return parser

# Does all the command handling
def process_commands(args, expenses):
    if args.command == "add":
        expense = Expense(args.description, args.amount)
        print(f"Expense added successfully (ID: {expense.id})")
        expenses.append(expense)

    if args.command == "list":
        print("ID Date Description Amount")
        for expense in expenses:
            print(f"{expense.id} {expense.date} {expense.description} {expense.amount:.2f}")

    if args.command == "summary":
        if args.month:  # If the --month argument was used
            month_name = calendar.month_name[args.month]
            monthly_expenses = [e for e in expenses if e.date.month == args.month]
            total = sum(e.amount for e in monthly_expenses)
            print(f"Total for {month_name}: ${total:.2f}")
        else:
            total = sum(e.amount for e in expenses)
            print(f"Total expenses: ${total:.2f}")

def save_expenses(expenses, filepath):
    with open(filepath, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)

def load_expenses(filepath):
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return []
    expenses = [Expense.from_dict(d) for d in data]
    Expense._id_counter = max((e.id for e in expenses), default=0) + 1
    return expenses

def main():
    # Stores a list of expenses
    expenses = load_expenses("expenses.json")

    parser = create_parser()
    args = parser.parse_args()
    process_commands(args, expenses)
    save_expenses(expenses, "expenses.json")

if __name__ == '__main__':
    main()