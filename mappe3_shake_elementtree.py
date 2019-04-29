import xml.etree.ElementTree as et
import xml.dom.minidom as xml
import re

file = open("shake.txt", mode="r", encoding="utf-8")
readfile = file.read()
file.close()

xml_declaration = """
<?xml version="1.0" encoding="UTF-8"
standalone="yes"?>
"""

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

# several loops to divide the text into sublists so we can count stanzas, lines and words
stanzalist = []
for stanzas_ in readfile.split("\n\n"):
    stanzalist.append(stanzas_)

stanza_lists = []
for stanzas in stanzalist:
    word_split = stanzas.split("\n")
    stanza_lists.append(word_split)

final_list = []
for lines in stanza_lists:
    for words in lines:
        splittt = words.split()
        final_list.append(splittt)

# divides lines into stanzas if in 6th position
final_list = [final_list[i:i + 6] for i in range(0,len(final_list), 6)]

# empty token counters
first_word_counter = 0
second_word_counter = 0
third_word_counter = 0
fourth_word_counter = 0


# using ElementTree we can set elements, subelements, their text elements and/or attributes using nested loops.
# enumerate() is important here so that we know which stanza and line we are on
poem = et.Element("poem") # root element "poem"
for stanzanumber, stanzas in enumerate(final_list,1):
        stanza = et.SubElement(poem, "stanza") # creates subelements stanza
        stanza.set("s-id", str(stanzanumber)) # gives the stanza elements an s-id attribute with number based on the enumeration
        for line_number, line in enumerate(stanzas,1): # looping through lines in stanzas, to identify which rhyme they belong to
            # looping further to get tokens. 
            # creates subelements depending on which stanza the word is in, and also counts the token for each stanza
            for token_number, token_word in enumerate(line,1): 
                if stanzanumber == 1:
                    first_word_counter += 1
                    token = et.SubElement(stanza, "token")
                    token.set("t-id", (f"""{stanzanumber}-{first_word_counter}"""))
                elif stanzanumber == 2:
                    second_word_counter += 1
                    token = et.SubElement(stanza, "token")
                    token.set("t-id", (f"""{stanzanumber}-{second_word_counter}"""))
                elif stanzanumber == 3:
                    third_word_counter += 1
                    token = et.SubElement(stanza, "token")
                    token.set("t-id", (f"""{stanzanumber}-{third_word_counter}"""))
                elif stanzanumber == 4:
                    fourth_word_counter += 1
                    token = et.SubElement(stanza, "token")
                    token.set("t-id", (f"""{stanzanumber}-{fourth_word_counter}"""))    
                # creates the subelement wordform            
                wordform = et.SubElement(token, "wordform")
                wordform.text = token_word      
                # since we know that the poem is a sestain with the rhyme scheme of AABCCB, we can assign
                # the rhyme element depending on the current line from enumerate
                rhyme = et.SubElement(token, "rhyme")
                if line_number == 1 or line_number == 2:
                    rhyme.text = "A"
                elif line_number == 3 or line_number == 6:
                    rhyme.text = "B"
                elif line_number == 4 or line_number == 5:
                    rhyme.text = "C"
            
# creates the element root tree from the first element, <poem>
tree = et.ElementTree(poem)
root = tree.getroot()

# the XML minidom creates a "pretty" XML string, which we can then send to a variable
xmlstr = xml.parseString(et.tostring(root,encoding="UTF-8")).toprettyxml(indent = "  ")
# using regex to remove the automatic XML declaration injected by etree so we can instead put it at the top where it should be
xmlstring=re.sub("\\<\\?xml(.+?)\\?\\>", "", xmlstr)


# prints the XML declaration, DTD and the XML string
print(f"""
{xml_declaration}
{dtd}

{xmlstring}
""")