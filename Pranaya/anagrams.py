#Create a function which accepts list of strings as input. The fxn should return subset of the list and remve any duplicates , even if they are duplicated by anagramming.
def remove_duplicate_anagrams(strings):
    unique_strings = set()
    sorted_strings = set()

    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in sorted_strings:
            unique_strings.add(string)
            sorted_strings.add(sorted_string)
    
    return unique_strings


input_list = ['abc', 'dire', 'cab', 'this', 'his']
result = remove_duplicate_anagrams(input_list)
print(result)