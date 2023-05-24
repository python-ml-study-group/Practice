import re
from collections import defaultdict

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

