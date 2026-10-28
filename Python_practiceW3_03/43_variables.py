#Write a Python program to split a list into different variables.
my_list = [1,2,3]
# a,b,c = my_list
# print(a)
# print(b)
# print(c)

def split_list(items):
    for item in items:
        print(item)

split_list(my_list)