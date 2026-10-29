#Sum Items in List
#Write a Python program to sum all the items in a list.

my_list = [1,2,3,5]

def sum_list(items):
    total = 0
    for i in items:
        total+=i
    return total

print(sum_list(my_list))