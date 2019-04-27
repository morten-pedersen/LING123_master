import xml.etree.ElementTree as et
import xml.dom.minidom as xml

file = open("shake.txt", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

poem_stanzas = readfile.split("\n\n")
poem_lines = readfile.split("\n")
poem_words = readfile.split()

for stanzanumber, stanzas in enumerate(poem_stanzas,1):
    print(stanzanumber,stanzas)

Stanza1_index = list(range(1,7))
Stanza2_index = list(range(8-14))
Stanza3_index = list(range(15-21))
Stanza4_index = list(range(22-27))

Stanza1 = []
Stanza2 = []
Stanza3 = []
Stanza4 = []



# for line_number, lines in enumerate(poem_lines,1):
#     print(line_number, lines)
#     if line_number in Stanza1_index:
#         Stanza1.append(lines)
#     elif line_number in Stanza2_index:
#         Stanza2.append(lines)
#     elif line_number in Stanza3_index:
#         Stanza3.append(lines)
#     elif line_number in Stanza4_index:
#         Stanza4.append(lines)

# for word_number, words in enumerate(poem_words,1):
#     print(word_number,words)

# print(f"""
# Stanza1: {Stanza1}
# Stanza2: {Stanza2}
# Stanza3: {Stanza3}
# Stanza4: {Stanza4}
# """)

# print(poem_words)


# stanza_id = "2"
# token_id = "2-25"
# wordform_text = "Birds"
# rhyme_text = "A"

# poem = et.Element("poem")
# stanza = et.SubElement(poem, "stanza")
# stanza.set("s-id", stanza_id)
# token = et.SubElement(stanza, "token")
# token.set("t-id", token_id)
# wordform = et.SubElement(token, "wordform")
# wordform.text(wordform_text)
# rhyme = et.SubElement(token, "rhyme")
# rhyme.text(rhyme_text)

# print(poem)
