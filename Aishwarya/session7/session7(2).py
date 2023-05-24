import unittest
def calculate_average(num):
    if len(num)==0:
        return 0
    total=sum(num)
    avg=total/len(num)
    return avg

class TestCalculateAverage(unittest.TestCase):
    def test_empty_list(self):
          self.assertEqual(calculate_average([]),0)

    def test_single_element(self):
          self.assertEqual(calculate_average([5]),5)

    def test_positive_numbers(self):
          self.assertEqual(calculate_average([1,2,3,4,5]),3)

    def test_negative_numbers(self):
          self.assertEqual(calculate_average([-1,-2,-3,-4,-5]),-3)

    def test_mixed_numbers(self):
          self.assertEqual(calculate_average([1,-2,3,-4,5]),0.6)                  


if __name__ == '__main__':
    unittest.main()


 