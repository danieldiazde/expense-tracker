import calendar
from utils import load_data, save_expenses, id_maker, now_iso, find_expense, find_expense_by_month
import tabulate

def add_expense(description: str, amount: float):
    data = load_data()
    new_id = id_maker(data)
    data.append({
        'ID': new_id,
        'Date': now_iso(),
        'Description': description.strip(),
        'Amount': amount
    })
    save_expenses(data)
    print(f"✅ Expense '{description}' of ${amount:.2f} saved successfully!")

def list_expenses():
    data = load_data()
    for row in data:
        row['Amount'] = f"${float(row['Amount']):.2f}"
    print(tabulate.tabulate(data, headers='keys', tablefmt='fancy_grid'))

def delete_expense(expense_id: int):
    data = load_data()
    expense = find_expense(expense_id, data)
    if not expense:
        print(f"❌ Expense with ID {expense_id} not found.")
        return
    new_data = [x for x in data if int(x['ID']) != expense_id]
    save_expenses(new_data)
    print(f"🗑️ Deleted expense #{expense_id}: '{expense['Description']}'")

def summary_expenses(month_filter: int | None = None):
    data = load_data()
    if not month_filter:
        total = sum(float(x['Amount']) for x in data)
        print(f"💰 Total expenses: ${total:.2f}")
    else:
        expenses = find_expense_by_month(month_filter)
        total = sum(float(x['Amount']) for x in expenses)
        print(f"📅 Total for {calendar.month_name[month_filter]}: ${total:.2f}")
