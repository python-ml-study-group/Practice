'''create a function which accepts the list of strings as input.
The function should return the subset of  the list and remove any duplicates.
even if they are duplicate by anagramming.
Ex: ['abc','dire','cab','this','his']
Return {'abc','dire','this','his'}'''


strings = ['abc', 'dire', 'cab', 'this', 'his']
def remove_duplicates(strings):
    unique_strings = set()

    for word in strings:
        # Convert the word to a sorted tuple of characters
        sorted_word = tuple(sorted(word))

        # Add the sorted word to the set of unique strings
        unique_strings.add(sorted_word)

    # Convert the set of tuples back to a set of strings
    unique_strings = set(''.join(word) for word in unique_strings)

    return unique_strings

unique_strings = remove_duplicates(strings)
print(unique_strings)