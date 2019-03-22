from codecs import open
from collections import Counter

# make sure that ttr_input.txt is in the same directory as the python file
file_in = open("pos_input.txt","r","utf-8")
# reads and closes the text file, and then splits it into tokens using split()
text_file = file_in.read()
file_in.close()

text = text_file.split()

# splits words on forward slash, and adds the word + the word type together
text = list((words.split("/")[0], words.split("/")[1]) for words in text)

noun = ["NOUN", "PRON", "PROPN"]
punctuation = ["PUNCT"]

frequencies = list()
previous_element = None

for current_element in text:
    if current_element[1] in noun and previous_element and previous_element[1] in punctuation:
        frequencies.append((previous_element, current_element))
    previous_element = current_element

counted_frequencies = Counter(frequencies)

for element,count in counted_frequencies.items():
    print(element, count)