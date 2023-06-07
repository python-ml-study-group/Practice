def count_and_print_occurrences(value, parameter, count=0):
    if isinstance(parameter, dict):
        for val in parameter.values():
            count = count_and_print_occurrences(value, val, count)
    elif isinstance(parameter, (list, tuple)):
        for item in parameter:
            count = count_and_print_occurrences(value, item, count)
    elif parameter == value:
        count += 1

    return count

def print_occurrence_count(value, parameter):
    count = count_and_print_occurrences(value, parameter)
    print("Occurrences:", count)
parameter = {
    'a': [1, 2, 3, 4],
    'b': {
        'c': 1,
        'd': [1, 2, 1, 3],
        'e': [4, 5, 6]
    }
}

value_to_search = 1

print_occurrence_count(value_to_search, parameter)
