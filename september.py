lyrics = "Do you remember 21st night of September ? Love was changing the mind of pretenders While chasing the clouds away Our hearts were ringing In the key that our souls were singing As we danced in the night Remember how the stars stole the night away yeah yeah yeah Hey hey hey Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day Ba duda ba duda ba duda badu Ba duda badu ba duda badu Ba duda badu ba duda yeah My thoughts are with you Holding hands with your heart to see you Only blue talk and love Remember how we knew love was here to stay Now December Found the love we shared in September Only blue talk and love Remember the true love we share today Hey hey hey Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya golden dreams were shiny days Now our bell was ringing aha Our souls was singing Do you remember every cloudy day yau There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya golden dreams were shiny days Ba de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya de ya"



lyrics = lyrics.lower().split()

trigrams = []

i = 0
while i < len(lyrics)-2:
    trigrams.append(lyrics[i]+"_"+lyrics[i+1]+"_"+lyrics[i+2])
    i += 1

trigram_frequency = {}

for trigram in trigrams:
    if trigram in trigram_frequency.keys():
        trigram_frequency[trigram] += 1
    else:
        trigram_frequency[trigram] = 1

sort_frequencies = sorted(trigram_frequency.items(), key=lambda x: x[1], reverse=True)

for entry in sort_frequencies:
    print(entry[0]+"\t"+str(entry[1]))
