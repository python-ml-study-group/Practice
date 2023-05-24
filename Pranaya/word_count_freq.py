#You are given a list of sentences as input. Your task is to create a program that counts the frequency of each word in the sentences and returns a dictionary with the word as the key and its frequency as the value. You should ignore case sensitivity and punctuation while counting the words. python program
#re module is used to remove punctuations
import re
from collections import Counter

sentences = [
    "I got my Job.",
    "I am searching for my job."
]

def word_count_frequency(sentences):
    word_frequency = Counter()
    for sentence in sentences:
        # lower() is used to convert to lower cases
        sentence = re.sub(r'[^\w\s]', '', sentence.lower())
        words = sentence.split() #splitting sentence into individual words
        word_frequency.update(words)
    
    return dict(word_frequency)

result = word_count_frequency(sentences)
print(result)
