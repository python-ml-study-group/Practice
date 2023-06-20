from expense import Expense
def input():
    pass

def calcualte():
    pass

def report (expenses):
    total_amount = sum(expenses)
    average_expense = total_amount / len(expenses)
    highest_expense = max(expenses)

    summary_report = f"Expense Summary\n\n"
    summary_report += f"Total amount spent: ${total_amount}\n"
    summary_report += f"Average expense: ${average_expense:.2f}\n"
    summary_report += f"Highest expense: ${highest_expense}\n"
    return summary_report
