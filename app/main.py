from fastapi import FastAPI 
from app.services import save_expense
from app.models import Expense
app = FastAPI()

@app.get("/")
def home():
    return{"message": "Expense Tracker API is running"}


@app.post("/expenses")
def add_expense(expense: Expense):
    save_expense(expense)
    return expense


@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    return {"message": "Update expense"}
