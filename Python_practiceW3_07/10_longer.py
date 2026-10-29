#Find Words Longer Than n
my_list = ['cat','xo','cake']
n=2

def words_longer(words):
    for word in words:
        if len(word)>n:
            print(word)

words_longer(my_list)