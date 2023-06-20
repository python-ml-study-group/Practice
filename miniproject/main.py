from expense import Expense
def input_validation():
    while True:
        try:
            amount = int(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input..... Please enter a valid expense amount.")
    
    return amount, category
amount, category = input_validation()
print("Expense amount:", amount)
print("Expense category:", category)

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

