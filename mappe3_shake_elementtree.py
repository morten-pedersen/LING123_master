import xml.etree.ElementTree as et
import xml.dom.minidom as xml
import re

file = open("shake.txt", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

poem_lines = readfile.split("\n")
# poem_lines = re.sub("\'\', ", "", str(poem_lines))
# print(poem_lines)

stanzalist = []

for stanzass in readfile.split("\n\n"):
    stanzalist.append(stanzass)

# print(stanzalist)

stanza_lists = []

for stanzas in stanzalist:
    word_split = stanzas.split()
    stanza_lists.append(word_split)


A_index = [0,1,7,8,14,15,21,22]
B_index = [2,5,9,12,16,19,23,26]
C_index = [3,4,10,11,17,18,24,25]

A_words = []
B_words = []
C_words = []

A_dict = {}
B_dict = {}
C_dict = {}

for line_count, lines in enumerate(poem_lines):
    lines = lines.split()
    if line_count in A_index:
        A_dict.setdefault('A', []).append(lines)
    elif line_count in B_index:
        B_dict.setdefault('B', []).append(lines)
    elif line_count in C_index:
        C_dict.setdefault('C', []).append(lines)

print(A_dict)
print(B_dict)
print(C_dict)


# print(f"""
# A: {A_words}
# B: {B_words}
# C: {C_words}
# """)



poem = et.Element("poem")
for stanzanumber, stanzas in enumerate(stanza_lists,1):
    stanza = et.SubElement(poem, "stanza")
    stanza.set("s-id", str(stanzanumber))
    for token_number, token_word in enumerate(stanzas,1):
        # print(token_word)
        token = et.SubElement(stanza, "token")
        token.set("t-id", (f"""{stanzanumber}-{token_number}"""))
        wordform = et.SubElement(token, "wordform")
        wordform.text = token_word
        rhyme = et.SubElement(token, "rhyme")
        rhyme.text(rhyme_text)

tree = et.ElementTree(poem)

tree.write("shake.xml")

root = tree.getroot()

xmlstr = xml.parseString(et.tostring(root)).toprettyxml(indent = "  ")
with open("shake.xml", "wb") as f:
    f.write(xmlstr)