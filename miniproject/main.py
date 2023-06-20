from expense import Expense
def input():
    pass

def calcualte(expense):
    total_expenses = sum(expense)
    average_expense = total_expenses / len(expense)
    highest_expense = max(expense)
    
    return {
        "total_expenses": total_expenses,
        "average_expense": average_expense,
        "highest_expense": highest_expense
    }

   

def report ():
    pass

