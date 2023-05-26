#Implement a
# function called calculate_average
# that takes in a list of numbers and
# returns their average. Write unit
# tests to verify the correctness of
# the function.

# avg= sum of all the values divided by the total number of values
def cal_avg(numbers):
    if not numbers:
        return 0  # Return 0 for  empty list
    
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

# Unit tests
def test_calculate_average(): #function to test
    # Test case 1: Average of positive numbers
    numbers = [1, 2, 3, 4, 5]
    expected_result = 3.0
    assert cal_avg(numbers) == expected_result
    
    # Test case 2: Average of negative numbers
    numbers = [-1, -2, -3, -4, -5]
    expected_result = -3.0
    #assert used to check if the result obtained is equal to the expected result.
    assert cal_avg(numbers) == expected_result
    
    # Test case 3: Average of mixed positive and negative numbers
    numbers = [-1, 2, -3, 4, -5]
    expected_result = -0.6
    assert cal_avg(numbers) == expected_result
    
    # Test case 4: Average of a single number
    numbers = [10]
    expected_result = 10.0
    assert cal_avg(numbers) == expected_result
    
    # Test case 5: Average of an empty list
    numbers = []
    expected_result = 0
    assert cal_avg(numbers) == expected_result
    
    print("All tests pass")

# Run the unit tests
test_calculate_average()
