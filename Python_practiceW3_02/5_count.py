#Count Strings with Same Start and End
def match_words(words):
    ctr = 0
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
    return ctr
print("Total no of matching words", match_words(['wow', 'mum', 'cat']))
