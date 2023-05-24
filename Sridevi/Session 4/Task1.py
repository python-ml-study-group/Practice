'''You are given a list of sentences as input. 
Your task is to create a program that counts the frequency of each word in the sentences
and returns a dictionary with the word as the key and its frequency as the value.
 You should ignore case sensitivity and punctuation while counting the words.'''


    
import re
from collections import defaultdict

   #List of sentences  
sentences = [                                                  
    'you are given a list', 
    'you have to create a program',
    'You have to do it on yourself.'
]

def count_frequency_of_words(sentences):                         #creates function for counting word frequency
    frequency_of_words = defaultdict(int)                        #created empty dictionary for the final results

    for sentence in sentences:
        # Remove punctuation and convert to lowercase
        sentence = re.sub(r'[^\w\s]', '', sentence).lower()

        # Split the sentence into words
        words = sentence.split()

        # Count the frequency of each word
        for word in words:
            frequency_of_words[word] += 1

    return dict(frequency_of_words)


count_frequency_of_words = count_frequency_of_words(sentences)  #calling the funtion
print(count_frequency_of_words)