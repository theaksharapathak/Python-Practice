#Write a Python program to find the list of words that are longer
#  than n from a given list of words.
my_list = ['cat','boy', 'elephant']
n = int(input("Enter a no:"))

def find_words(words):
    for word in words:
        if len(word)>n:
            print(word)

find_words(my_list)