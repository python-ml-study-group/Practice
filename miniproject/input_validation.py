from expense import Expense
def input_():
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
