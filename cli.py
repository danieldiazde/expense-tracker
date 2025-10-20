import argparse
from core import add_expense, list_expenses, summary_expenses, delete_expense

parser = argparse.ArgumentParser(description='Expense Tracker CLI Application')
subparsers = parser.add_subparsers(dest='command', required=True)

# Add command
add_parser = subparsers.add_parser('add', help='Record a new expense.')
add_parser.add_argument('--description', required=True, help='Description of the expense.')
add_parser.add_argument('--amount', type=float, required=True, help='Amount spent.')

# List command
subparsers.add_parser('list', help='List all recorded expenses.')

# Summary command
summary_parser = subparsers.add_parser('summary', help='Show summary of expenses.')
summary_parser.add_argument('--month', type=int, help='Filter by month number (1–12).')

# Delete command
delete_parser = subparsers.add_parser('delete', help='Delete an expense by ID.')
delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete.')

def main():
    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.description, args.amount)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'summary':
        summary_expenses(args.month)
    elif args.command == 'delete':
        delete_expense(args.id)

if __name__ == "__main__":
    main()
