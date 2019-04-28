poem = et.Element("poem")
# for stanzanumber, stanzas in enumerate(stanza_lists,1):
#     stanza = et.SubElement(poem, "stanza")
#     stanza.set("s-id", str(stanzanumber))
#     for token_number, token_word in enumerate(stanzas,1):
#         # print(token_word)
#         token = et.SubElement(stanza, "token")
#         token.set("t-id", (f"""{stanzanumber}-{token_number}"""))
#         wordform = et.SubElement(token, "wordform")
#         wordform.text = token_word        
#         rhyme = et.SubElement(token, "rhyme")
#         if token_word in A_dict.get('A', token_word):
#             rhyme.text = "A"
#         elif token_word in B_dict.get('B', token_word):
#             rhyme.text = "B"
#         elif token_word in C_dict.get('C', token_word):
#             rhyme.text = "C"