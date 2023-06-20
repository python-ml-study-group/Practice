from expense import Expense
from main import calculate
from unittest import TestCase

class TestExpense(TestCase):
    @TestCase
    def test_calculate(self):
        # Arrange
        expense = Expense()

        # Act
        actual = expense.calculate()
        # Assert
        self.assertEqual(0, actual)
if __name__ == "__main__":
    TestCase.main()
    