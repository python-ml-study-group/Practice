from expense import Expense
def input_(expenses):
    while True:
        try:
            ex = Expense()
            ex.amount = int(input("Enter the expense amount: "))
            ex.category = input("Enter the expense category: ")
            expenses.append(ex)
        except ValueError:
            print("Invalid input..... Please enter a valid expense amount.")
    return True

def calcualte(expenses):
    total_expenses = sum(expense)
    average_expense = total_expenses / len(expense)
    highest_expense = max(expense)
    
    return {
        "total_expenses": total_expenses,
        "average_expense": average_expense,
        "highest_expense": highest_expense
    }

   

def report (calc):
    total_amount = sum(expenses)
    average_expense = total_amount / len(expenses)
    highest_expense = max(expenses)

    summary_report = f"Expense Summary\n\n"
    summary_report += f"Total amount spent: ${total_amount}\n"
    summary_report += f"Average expense: ${average_expense:.2f}\n"
    summary_report += f"Highest expense: ${highest_expense}\n"
    return summary_report

def main():
    expenses = []
    input_(expenses)
    calc = calcualte(expenses)
    report(calc)
    print(report(expenses))
