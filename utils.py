import csv
import os
import datetime

FILE = os.path.join(os.path.dirname(__file__), "data", "expense_tracker.csv")
header_fieldnames = ['ID', 'Date', 'Description', 'Amount']

def now_iso():
    return datetime.date.today().strftime('%Y-%m-%d')

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)

def save_expenses(expenses: list):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header_fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def id_maker(expenses: list):
    return 1 if not expenses else max(int(x['ID']) for x in expenses) + 1

def find_expense(expense_id: int, expenses_list: list):
    for expense in expenses_list:
        if int(expense['ID']) == expense_id:
            return expense
    return None

def find_expense_by_month(month: int):
    data = load_data()
    return [
        x for x in data
        if datetime.datetime.strptime(x['Date'], '%Y-%m-%d').month == month
    ]
