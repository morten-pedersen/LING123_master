from codecs import open as o

##### type / token - ratio = (number of types / number of tokens) * 100 #####

file_in = o("ttr_input.txt","r","utf-8")

text = file_in.read()

file_in.close()

print(text)