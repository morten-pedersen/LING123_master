import xml.etree.ElementTree as et
import xml.dom.minidom as xml
import re

file = open("shake.txt", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

dtd = """
<!DOCTYPE poem [
<!ELEMENT poem (stanza+) >
<!ELEMENT stanza (token+) >
<!ATTLIST stanza s-id CDATA #REQUIRED >
<!ELEMENT token (wordform,rhyme) >
<!ATTLIST token t-id CDATA #REQUIRED >
<!ELEMENT wordform (#PCDATA) >
<!ELEMENT rhyme (#PCDATA) >
]"""

poem_lines = readfile.split("\n")
poem_lines = re.sub("\'\', ", "", str(poem_lines))
# print(poem_lines)

stanzalist = []

for stanzass in readfile.split("\n\n"):
    stanzalist.append(stanzass)

# print(stanzalist)

stanza_lists = []

for stanzas in stanzalist:
    word_split = stanzas.split()
    stanza_lists.append(word_split)

text = []
for line in readfile.split('\n'):
  sentences = []
  for sentence in line.split('.'):
    words = []
    for word in sentence.split(' '):
      if len(word.strip()) > 0: # make sure we are adding something
        words.append(word.strip())
    if len(words) > 0:
      sentences.append(words)
  if len(sentences) > 0:
    text.append(sentences)

# print(text)

A_index = [0,1,6,7,12,13,18,19]
B_index = [2,5,8,11,14,17,20,23]
C_index = [3,4,9,10,15,16,21,22]

A_words = []
B_words = []
C_words = []

A_dict = {}
B_dict = {}
C_dict = {}

# for line_count, lines in enumerate(poem_lines):
#     lines = lines.split()
#     if line_count in A_index:
#         A_dict.setdefault('A', []).append(lines)
#         # A_words.append(lines)
#     elif line_count in B_index:
#         B_dict.setdefault('B', []).append(lines)
#         # B_words.append(lines)
#     elif line_count in C_index:
#         C_dict.setdefault('C', []).append(lines)
#         # C_words.append(lines)

# print(A_dict)
# print(B_dict)
# print(C_dict)


# print(f"""
# A: {A_words}
# B: {B_words}
# C: {C_words}
# """)

# print(A_dict.values())

# for key, values in A_dict.items():
#     print(key, values)

# print(type(A_dict.values()))

flat_a = [item for sublist in A_words for item in sublist]
flat_b = [item for sublist in B_words for item in sublist]
flat_c = [item for sublist in C_words for item in sublist]

# print(poem_lines.spl)



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
        for line_count, lines in enumerate(text):
            # print(line_count, lines)
            if line_count in A_index:
                # print(line_count, "A")
                rhyme.text = "A"
            elif line_count in B_index:
                # print(line_count, "B")
                rhyme.text = "B"
            elif line_count in C_index:
                # print(line_count, "C")
                rhyme.text = "C"
                
        # if token_word in A_dict.values():
        #     rhyme.text = str(A_dict.keys())
        # elif token_word in B_dict.values():
        #     rhyme.text = str(B_dict.keys())
        # elif token_word in C_dict.values():
        #     rhyme.text = str(C_dict.keys())


tree = et.ElementTree(poem)

# tree.write("shake.xml")

root = tree.getroot()

xmlstr = xml.parseString(et.tostring(root)).toprettyxml(indent = "  ")
# with open("shake.xml", "w") as f:
#     f.write(xmlstr)

print(f"""{dtd}

{xmlstr}""")