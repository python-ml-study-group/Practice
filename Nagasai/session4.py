import re
from collections import defaultdict
task1

def count_word_frequency(sentences):
 word_frequency = defaultdict(int)
 for sentence in sentences:
  sentence = re.sub('[^\w\s]', '', sentence.lower())
  #print(sentence)
  words = sentence.split()
  #print(words)
  for word in words:
    word_frequency[word] += 1
 return word_frequency

 sentences = [
    "hello, how are you doing?",
     "hope you are doing good"
     ]

result = count_word_frequency(sentences)
print(result)

*************************************************
task 2

def remove_duplicates(strings):
    unique_strings = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))  # Sort the characters in the lowercase string
        unique_strings.add(sorted_string)  # Add the sorted string to the set

    return unique_strings
input_list = ['abc', 'dire', 'cab', 'this', 'his']
result = remove_duplicates(input_list)
print(result)
