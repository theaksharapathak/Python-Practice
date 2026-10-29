#Find Words Longer Than n
l = ['cat','elephant','whale']
n = 2

def find_words(words):
    for word in words:
        if len(word)>n:
            print(word)
find_words(l)