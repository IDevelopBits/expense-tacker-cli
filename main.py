import argparse
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
        expense.save("expenses.json")
    if args.command == "list":
        print("ID Date Description Amount")
    if args.command == "summary":
        total = sum([expense.amount for expense in expenses])

def main():
    # Stores a list of expenses
    expenses = []

    parser = create_parser()
    args = parser.parse_args()
    process_commands(args, expenses)

if __name__ == '__main__':
    main()