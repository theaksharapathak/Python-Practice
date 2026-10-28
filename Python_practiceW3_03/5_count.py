#Write a Python program to count the number of strings 
# from a given list of strings. The string length is 2 
# or more and the firstand last characters are the same.
my_list = ['mom','cat','wow']

def count_no(words):
    count = 0
    for w in words:
        if len(w)>2 and w[0] == w[-1]:
            count += 1
    return count
print("total no of strings:", count_no(my_list))
