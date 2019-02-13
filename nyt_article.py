# Source: https://www.nytimes.com/2019/02/04/us/politics/trump-border-wall-republicans.html
# Modified by Cho

import re

article = ["President Trump 's legislative path to a border wall has narrowed significantly on the eve of Tuesday 's State of the Union speech , and his fallback plan to circumvent Congress by declaring a state of emergency could create a major division in his own party .",
"As he prepares to make his case to the largest national audience of the year , Mr . Trump appeared to be in an increasingly precarious position , unable to sway the wider public to his cause and unwilling , at least so far , to apply the persuasion and compromise that have gotten previous presidents out of political jams .",
"Anxiety over the damage being inflicted on the party is growing .",
"Last week , in a one-on-one meeting with the president , Senator Mitch McConnell of Kentucky , the majority leader , reportedly warned Mr . Trump that declaring a national emergency to build his wall would almost certainly spark a rebellion within his party - and a vote to overrule him .",
"House and Senate negotiators have been moving toward a bipartisan agreement as early as Friday to keep the government funded after Feb . 15 - with or without the president 's support .",
"But the president 's supporters continue to plead for unity .",
"'This is the defining moment of his presidency , ' said Senator Lindsey Graham , a South Carolina Republican who is one of Mr . Trump 's biggest supporters on Capitol Hill , speaking at an event in Greenville on Monday .",
"'To every Republican , if you don't stand behind this president , we're not going to stand behind you when it comes to the wall , ' said Mr . Graham , adding that he feared ' a war within the Republican Party ' if Republicans did not support Mr . Trump 's plans , including an emergency declaration .",
"The president 's advisers have said the speech will focus on unity .",
"But he is also expected to double down on the wall .",
"In an Oval Office interview last week , he cast doubt on a settlement being hashed out by a bipartisan committee of 17 House members and senators before the Feb . 15 deadline , saying that anything short of his full demand would be ' a waste of time . '",
"At the same time , Mr . Trump continued to brandish the threat of an emergency declaration that would allow him to divert existing federal funding to the wall , an idea that has sparked heated opposition among Senate Republicans , who have grown increasingly comfortable in their defiance .",
"On Monday , the Senate formally adopted an amendment to a broader Middle East policy bill , 70 to 26 , that rebuked the president for what Republicans saw as a precipitous withdrawal of troops from Afghanistan and Syria ."]

def count_sentences_in_list(w):
    sentence_count = 0
    for sentence in article:
        sentence_count += 1
    print('Number of sentences: {}\n'.format(sentence_count))

def count_tokens(w):
    tokens = 0
    for sentence in article:
        tokens += len(sentence.split(' '))
    print('Number of tokens: {}'.format(tokens))
    # text = re.sub('[\[\]"\',.]', ' ', str(w))
    # print('Text:\n {} \n-------------------------------------------\nNumber of tokens: {}'.format(text, tokens))

# def doot(w):
#     if " '" in w:
#         text = re.sub(' ', '\'', w)
#     print(text)

def count_characters(w):
    characters = 0
    for sentence in article:
        characters += len(sentence)
    print('Number of characters: {}'.format(characters))

count_sentences_in_list(article)
count_tokens(article)
count_characters(article)
# doot(article)

