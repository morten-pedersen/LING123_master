# This line imports the square root function
# Use it with sqrt()
# Example: square root of 9 is:  sqrt(9)
from math import sqrt

# N-Grams
unigrams = ['i', 'have', 'been', 'one', 'acquainted', 'with', 'the', 'night', 'i', 'have', 'walked', 'out', 'in', 'rain', 'and', 'back', 'in', 'rain', 'i', 'have', 'outwalked', 'the', 'furthest', 'city', 'light', 'i', 'have', 'looked', 'down', 'the', 'saddest', 'city', 'lane', 'i', 'have', 'passed', 'by', 'the', 'watchman', 'on', 'his', 'beat', 'and', 'dropped', 'my', 'eyes', 'unwilling', 'to', 'explain', 'i', 'have', 'stood', 'still', 'and', 'stopped', 'the', 'sound', 'of', 'feet', 'when', 'far', 'away', 'an', 'interrupted', 'cry', 'came', 'over', 'houses', 'from', 'another', 'street', 'but', 'not', 'to', 'call', 'me', 'back', 'or', 'say', 'good-bye', 'and', 'further', 'still', 'at', 'an', 'unearthly', 'height', 'one', 'luminary', 'clock', 'against', 'the', 'sky', 'proclaimed', 'the', 'time', 'was', 'neither', 'wrong', 'nor', 'right', 'i', 'have', 'been', 'one', 'acquainted', 'with', 'the', 'night']
bigrams = ['i have', 'have been', 'been one', 'one acquainted', 'acquainted with', 'with the', 'the night', 'night i', 'i have', 'have walked', 'walked out', 'out in', 'in rain', 'rain and', 'and back', 'back in', 'in rain', 'rain i', 'i have', 'have outwalked', 'outwalked the', 'the furthest', 'furthest city', 'city light', 'light i', 'i have', 'have looked', 'looked down', 'down the', 'the saddest', 'saddest city', 'city lane', 'lane i', 'i have', 'have passed', 'passed by', 'by the', 'the watchman', 'watchman on', 'on his', 'his beat', 'beat and', 'and dropped', 'dropped my', 'my eyes', 'eyes unwilling', 'unwilling to', 'to explain', 'explain i', 'i have', 'have stood', 'stood still', 'still and', 'and stopped', 'stopped the', 'the sound', 'sound of', 'of feet', 'feet when', 'when far', 'far away', 'away an', 'an interrupted', 'interrupted cry', 'cry came', 'came over', 'over houses', 'houses from', 'from another', 'another street', 'street but', 'but not', 'not to', 'to call', 'call me', 'me back', 'back or', 'or say', 'say good', 'good bye', 'bye and', 'and further', 'further still', 'still at', 'at an', 'an unearthly', 'unearthly height', 'height one', 'one luminary', 'luminary clock', 'clock against', 'against the', 'the sky', 'sky proclaimed', 'proclaimed the', 'the time', 'time was', 'was neither', 'neither wrong', 'wrong nor', 'nor right', 'right i', 'i have', 'have been', 'been one', 'one acquainted', 'acquainted with', 'with the', 'the night']

token_1 = "have"
token_2 = "been"

def t_score(f1, f2, corpus, corpus_bigrams):
    
    # corpus_size is the length of the entered corpus, which in this case is the unigrams list
    corpus_size = len(corpus) 
    word_one_freq = 0 
    word_two_freq = 0
    observed_bigram_freq = 0
    
    # this loop iterates through the entered corpus (which in this case is the unigram list) and 
    # checks if any words matches the entered words (token_1 ("have") and token_2 ("been"))
    for word in corpus:       
        if word == token_1:
            word_one_freq += 1
        elif word == token_2:
            word_two_freq += 1
    
    # the expected bigram frequency is then calculated by Fe = F1 / Nc * F2
    expected_bigram_freq = (word_one_freq / corpus_size) * word_two_freq
    
    # this second loop iterates through the bigram list and checks for bigrams that matches the token_1 and token_2 when concatenated
    for bigram in corpus_bigrams:
        if bigram == token_1 + ' ' + token_2:
            observed_bigram_freq += 1
            
    # t-score is calculated by t = (F - Fe) / sqrt(F)
    t_score = (observed_bigram_freq - expected_bigram_freq) / sqrt(observed_bigram_freq)
    
    # prints all the information we want
    print(f"""
    Bigram to check for: "{token_1} {token_2}"
    F1: {word_one_freq}
    F2: {word_two_freq}
    Nc: {corpus_size}
    Fe: {expected_bigram_freq}
    F: {observed_bigram_freq}
    t-score: {t_score}
    """)   

# runs the function with all the necessary parameters
t_score(token_1, token_2, unigrams, bigrams)