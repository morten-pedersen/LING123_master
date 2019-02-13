word = "minoritetsladningsbaererdiffusjonskoeffisientmaalingsapparatur"

def countcharacters(w):
    print(f"There are {len(word)} characters in the string")

def n_count(w):
    n_occurrences = 0
    s_occurrences = 0
    n_and_s = 0
    for character in word:
        if character == "n":
            n_occurrences += 1
        elif character == "s":
            s_occurrences += 1
    n_and_s = n_occurrences + s_occurrences
    print('n count: {} \ns count: {} \nboth n and s: {}'.format(n_occurrences, s_occurrences, n_and_s))



n_count(word)
