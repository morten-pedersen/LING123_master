TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]

# vowels to be used to count syllables
vowels = "AEIOUaeiou"

def get_fres_score(text):
    vowel_count = 0
    word_count = 0
    sentence_count = 0

    # loops through the words in the sentences in the text, and counts the respective counters += 1 after each hit
    for sentence in text:
        sentence_count += 1
        words = sentence.split()
        for word in words:
            word_count += 1
            for letter in word:
                if letter in vowels:
                    vowel_count += 1
    
    fres_score = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (vowel_count / word_count))
    
    print(f"""
        Number of sentences: {sentence_count}
        Number of words: {word_count}
        Number of syllables: {vowel_count}
        FRES score: {fres_score}    
    """)

print("Chosen text: TEXT1")    
get_fres_score(TEXT1)
print("Chosen text: TEXT2")
get_fres_score(TEXT2)