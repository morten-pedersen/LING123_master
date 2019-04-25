file = open("shake.txt", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

print(readfile)

# rhyme = A, B
# 1: A, 2: B, 3: A, 4: A, 5: B, 6: B


print(f"""
<poem>
    <stanza s-id="{}"></stanza>
    <

""")
<poem>
    <stanza s-id="1"></stanza>
        <token t-id="1-2">
        <token t-id="1-3">
            <wordform>hence</wordform>
            <rhyme>A</rhyme>
    <stanza></stanza>
    <stanza></stanza>
    <stanza></stanza>
</poem>


<!DOCTYPE poem [
<!ELEMENT poem (stanza+) >
<!ELEMENT stanza (token+) >
<!ATTLIST stanza s-id CDATA #REQUIRED >
<!ELEMENT token (wordform,rhyme) >
<!ATTLIST token t-id CDATA #REQUIRED >
<!ELEMENT wordform (#PCDATA) >
<!ELEMENT rhyme (#PCDATA) >
]

#AABCCB