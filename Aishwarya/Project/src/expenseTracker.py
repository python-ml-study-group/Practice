class Expense:
    def __init__(self,date,amount,category):
        self.date=date
        self.amount=amount
        self.category=category

class Expenses:
    def __init__(self):
        self.expenseList=[]

    def add_expense(self,expense):
        self.expenseList.append(expense)

    def view(self):
        for expense in self.expenseList:
            print(expense.date)
            print(expense.amount)
            print(expense.category)

    def summary(self):
        try:

            l1=[expense.amount for expense in self.expenseList]
            averageExpense=sum(l1)/len(self.expenseList)*100
            maxExpense=max(l1)   
            minExpense=min(l1)
            print("AverageExpense: ",averageExpense)
            print("Maximum Expense: ",maxExpense) 
            print("Minimum Expense: ",minExpense)
            return averageExpense,maxExpense,minExpense

        except ZeroDivisionError as e:
            print("Select atleast one item")


def main():
    tracker = Expenses()

    while True:
        print("Expense Tracker")
        print("1.Add an expense")
        print("2.View expenses")
        print("3.View summary")
        print("4.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date: ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")

            expense = Expense(date, amount, category)
            tracker.add_expense(expense)
            print("Expense added successfully")

        elif choice == "2":
            print("Expenses:")
            tracker.view()

        elif choice == "3":
            print("Summary:")
            tracker.summary()

        elif choice == "4":
            print("Exit")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()                  

