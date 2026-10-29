#Sum Items in List
#Write a Python program to sum all the items in a list.

l = [1,22,3]

def sum_list(items):
    total = 0
    for i in items:
        total+= i
    return total

print(sum_list(l))