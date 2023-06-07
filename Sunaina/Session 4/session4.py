"""Task 1: You are given a list of sentences as input. Your task is to create a program that counts the
frequency of each word in the sentences and returns a dictionary with the word as the key and its frequency as the value.
You should ignore case sensitivity and punctuation while counting the words. - with group by function"""

import itertools
import string

sentences = [
    "The sun Is shining and",
    "the sky So is blue",
    "the birds are flying",
    "And the breeze is so cool."
]

def count_word_frequency(sentences):
    word_frequency = {}

    # Join all sentences into a single string
    all_text = ' '.join(sentences)

    # Remove punctuation from the text
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = all_text.translate(translator)

    # Convert the text to lowercase
    lowercase_text = text_without_punctuation.lower()

    # Split the text into words
    words = lowercase_text.split()

    # Use groupby to count the frequency of each word
    grouped_words = itertools.groupby(sorted(words))

    for word, group in grouped_words:
        word_frequency[word] = len(list(group))

    return word_frequency

frequency = count_word_frequency(sentences)
print(frequency)


""" Task 2: Create a function which accepts the list of strings as input. The function should return the set of anagram, and if there are duplicates, do not include.
Ex. ['abc', 'dire', cab', 'this', his] and it should return {'abc', 'dire', 'this', his)"""

list_of_strings = ['abc', 'dire', 'cab', 'this', 'his']

def find_unique_anagrams(strings):
    anagrams = set()
    unique_anagrams = []  

    # Iterating over each word in the list
    for word in list_of_strings:  
        sorted_word = ''.join(sorted(word))  
        if sorted_word not in anagrams:  
            unique_anagrams.append(word)
            
            # Adding the sorted word to the set of anagrams
            anagrams.add(sorted_word)  

    return unique_anagrams 

# Calling the function with the list of strings
unique_anagrams = find_unique_anagrams(list_of_strings)

# Printing the resulting unique anagrams
print(unique_anagrams)  








