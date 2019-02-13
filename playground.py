def comparison(w1, w2):
    print("w1: " + w1 + "\n" + "w2: " + w2)

    if w1 == w2:
        print("The words are identical")
        
    if len(w1) > len(w2):
        print("w1 is longer than w2")

    if len(w2) > len(w1):
        print("w2 is longer than w1")

    if len(w1) == len(w2):
        print("Words are of equal length")

    if w1 > w2:
        print("w1 follows w2 alphabetically")

    if w1 < w2:
        print("w2 follows w1 alphabetically")

comparison("abc", "bcde")



    

    

    

    