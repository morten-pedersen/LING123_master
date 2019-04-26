file = open("shake.txt", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

# print(readfile)

poem = readfile.split("\n")





A_index = [0,1,7,8,14,15,21,22]
B_index = [2,5,9,12,16,19,23,26]
C_index = [3,4,10,11,17,18,24,25]
Stanza1_index = [0,1,2,3,4,5]
Stanza2_index = [7,8,9,10,11,12]
Stanza3_index = [14,15,16,17,18,19]
Stanza4_index = [21,22,23,24,25,26]

Stanza1 = []
Stanza2 = []
Stanza3 = []
Stanza4 = []
A = []
B = []
C = []

poem_start_xml = "<poem>"
poem_end_xml = "</poem>"
stanza_start_xml = "<stanza>"
stanza_end_xml = "</stanza>"
token_start_xml = "<token>"
token_end_xml = "</token>"

stanza = ""
poem_final = ""

for sentence in poem:
    # print(poem.index(sentence))
    if poem.index(sentence) in A_index:
        A.append(sentence)
    elif poem.index(sentence) in B_index:
        B.append(sentence)
    elif poem.index(sentence) in C_index:
        C.append(sentence)

for sentence in poem:
    # print(poem.index(sentence))
    if poem.index(sentence) in Stanza1_index:
        Stanza1.append(sentence)
        stanza += f"<stanza s-id=1{Stanza1}</stanza>\n"
    elif poem.index(sentence) in Stanza2_index:
        Stanza2.append(sentence)
        stanza += f"<stanza s-id=2{Stanza2}</stanza>\n"
    elif poem.index(sentence) in Stanza3_index:
        Stanza3.append(sentence)
    elif poem.index(sentence) in Stanza4_index:
        Stanza4.append(sentence)
    print(poem_final)



# print(f"""
# Sentences in rhyme A: {A} \n
# Sentences in rhyme B: {B} \n
# Sentences in rhyme C: {C} \n

# Stanza 1: {Stanza1}
# Stanza 2: {Stanza2}
# Stanza 3: {Stanza3}
# Stanza 4: {Stanza4}
# """)
    





# <poem>
#     <stanza s-id="1"></stanza>
#         <token t-id="1-2">
#         <token t-id="1-3">
#             <wordform>hence</wordform>
#             <rhyme>A</rhyme>
#     <stanza></stanza>
#     <stanza></stanza>
#     <stanza></stanza>
# </poem>


# <!DOCTYPE poem [
# <!ELEMENT poem (stanza+) >
# <!ELEMENT stanza (token+) >
# <!ATTLIST stanza s-id CDATA #REQUIRED >
# <!ELEMENT token (wordform,rhyme) >
# <!ATTLIST token t-id CDATA #REQUIRED >
# <!ELEMENT wordform (#PCDATA) >
# <!ELEMENT rhyme (#PCDATA) >
# ]

# #AABCCB