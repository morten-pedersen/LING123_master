from codecs import open

##### type / token - ratio = (number of types / number of tokens) * 100 #####

# make sure that ttr_input.txt is in the same directory as the python file
file_in = open("ttr_input.txt","r","utf-8")

# reads and closes the text file, and then splits it into tokens using split()
text = file_in.read()

file_in.close()

text = text.split()

# tokens are the length of the text list, 
# while we find unique words using set (sets can only contain unique objects)
token_count = len(text)
type_count = len(set(text)) 
ttr = (type_count / token_count) * 100

print(f"""
Number of tokens: {token_count}
Number of types: {type_count}
TTR-ratio: {ttr}
""")
