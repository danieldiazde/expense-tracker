# 💸 Expense Tracker CLI

A simple command-line **Expense Tracker** built with Python to record, list, and summarize your daily expenses — directly from the terminal.

---

## 🚀 Features
- Add new expenses with description and amount  
- View all expenses in a clean table  
- Delete expenses by ID  
- Get monthly or total summaries  
- Stores data locally in a CSV file  

---

## 🧩 How to Use

### 1️⃣ Add a new expense
Use the `add` command with a description and an amount.

```
python -m expense_tracker add --description "Groceries" --amount 45.80
```
✅ Output example:
```
Expense 'Groceries' of $45.80 saved successfully!
```
### 2️⃣ List all expenses
View all your recorded expenses in a neat table.

```
python -m expense_tracker list
```
📋 Example output:
```
╒════╤════════════╤═══════════════╤══════════╕
│ ID │ Date       │ Description   │ Amount   │
╞════╪════════════╪═══════════════╪══════════╡
│ 1  │ 2025-10-18 │ Groceries     │ $45.80   │
│ 2  │ 2025-10-19 │ Coffee        │ $3.50    │
╘════╧════════════╧═══════════════╧══════════╛
```
### 3️⃣ View your expense summary
See the total of all your expenses, or filter by month.

**Total summary:**
```
python -m expense_tracker summary
```
💰 Output:
```
Total expenses: $234.50
```
Monthly summary:
```
python -m expense_tracker summary --month 10
```
📅 Output:
```
Total expenses for October: $123.20
```
### 4️⃣ Delete an expense by ID
Remove an expense entry using its ID number.
```
python -m expense_tracker delete --id 2
```
🗑️ Output:
```
Successfully deleted expense #2: 'Coffee'
```
### 5️⃣ Check the CSV file
All data is stored automatically at:
```
expense_tracker/data/expense_tracker.csv
```
You can open it with Excel, Numbers, or any text editor to view your expenses.

### 🧰 Requirements
- Python 3.10+
- tabulate

Install dependencies with:
```
pip install -r requirements.txt
```