import unittest
from  expenseTracker import Expense,Expenses

class TestexpenseTracker(unittest.TestCase):
    def testadd_expense(self):
        expenses=Expenses()
        expenses.add_expense(Expense("12/02/2020",100,"food"))
        expenses.add_expense(Expense("15/02/2020",200,"food"))
        average,maxamt,minamt=expenses.summary()

        self.assertEqual(average,150,"average is not calculated properly")
        self.assertEqual(maxamt,200,"Max is not calculated properly")
        self.assertEqual(minamt,100,"min is not calculated properly")



if __name__=="__main__":
    unittest.main()

        

       




