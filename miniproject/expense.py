class Expense:
    def __init__(
        self,
        expense_records_list
    ):
        self.expense_records_list = []

    def addexpense(self, expense):
        self.expense_records_list.append(expense)

if __name__ == "__main__":
    expense = Expense()

