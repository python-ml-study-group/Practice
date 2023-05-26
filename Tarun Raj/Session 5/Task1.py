# You are given a list of sentences as input. Your task is to create a program
# that counts the frequency of each word in the sentences and returns a dictionary
# with the word as the key and its frequency as the value. You should ignore case
# sensitivity and punctuation while counting the words.

import re
from collections import Counter

def count_word_frequency(sentences):
    word_frequency = Counter()
    for sentence in sentences:
        sentence = re.sub(r'[^\w\s]', '', sentence.lower())
        words = sentence.split()
        word_frequency.update(words)

    return dict(word_frequency)

# list of sentences
sentences = [
    "I went to college today morning with my Friend.",
    "Even though the food was very spicy, my friend managed to eat it somehow!",
    "I went to temple also!"
]

frequency = count_word_frequency(sentences)
print(frequency)
