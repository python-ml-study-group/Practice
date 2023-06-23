import unittest
from expense import Expense
from main import calculate

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # Set up sample expenses for testing
        self.expenses = [
            {"amount": 100, "category": "Food"},
            {"amount": 50, "category": "Transportation"},
            {"amount": 200, "category": "Shopping"},
            {"amount": 75, "category": "Food"},
        ]

    def test_calculate_total_expenses(self):
        total_expenses = calculate_total_expenses(self.expenses)
        self.assertEqual(total_expenses, 425)

    def test_calculate_average_expense(self):
        average_expense = calculate_average_expense(self.expenses)
        self.assertEqual(average_expense, 106.25)

    def test_get_highest_expense(self):
        highest_expense = get_highest_expense(self.expenses)
        self.assertEqual(highest_expense, {"amount": 200, "category": "Shopping"})

    def test_get_highest_expense_empty_list(self):
        highest_expense = get_highest_expense([])
        self.assertIsNone(highest_expense)

if __name__ == '__main__':
    unittest.main()

    