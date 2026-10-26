#Find Words Longer Than n
my_list = ['cat','mouse','horse','elephant']
n = int(input("Enter a no n:"))

def find_words(items):
    required_words = []
    for item in items:
        if len(item) > n:
            required_words.append(item)
    return required_words

print("Words longer than n:", find_words(my_list))



