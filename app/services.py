import csv 

def save_expense(expense):
    with open("data/expenses.csv", "r", newline="") as file:
        rows = list(csv.reader(file))

    new_id = len(rows)

    with open("data/expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            new_id,
            expense.title,
            expense.amount,
            expense.category,
            expense.date,
            expense.notes
        ])

def update_expense(expense_id: int, expense):
    with open("data/expenses.csv", "r", newline="") as file:
     rows = list(csv.reader(file))

    for row in rows[1:]:
      if int(row[0]) == expense_id:
        row[1:] = [
           expense.title,
           expense.amount,
           expense.category,
           expense.date,
           expense.notes
        ]

    with open("data/expenses.csv", "w", newline="") as file:
       writer = csv.writer(file)
       writer.writerows(rows)

