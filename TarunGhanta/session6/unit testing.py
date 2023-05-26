def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

import unittest
class TestCalculateAverage(unittest.TestCase):

    def testlist_1(self):
        self.assertEqual(calculate_average([]), 0)

    def testlist_2(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def testlist_3(self):
        self.assertEqual(calculate_average([-1, -2, -3, -4, -5]), -3)

    def testlist_4(self):
        self.assertEqual(calculate_average([1, -2, 3, -4, 5]), 0.6)

if __name__ == '__main__':
    unittest.main()
