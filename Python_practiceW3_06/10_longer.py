#Find Words Longer Than n
#Write a Python program to find the list of words that are longer
#  than n from a given list of words.

my_list = ['cat','cake','elephant']
n=3

def words_longer(words):
    for word in words:
        if len(word) >n:
            print(word)

words_longer(my_list)