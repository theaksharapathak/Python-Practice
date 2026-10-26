# Write a Python program to create a list by concatenating a given
#  list with a range from 1 to n.
my_list = ['p', 'q', 'r']
n = int(input("Enter a no to concatenate:"))
new_list = []


def concat(items):
    for i in range(1, n+1):
        for j in items:
            new_list.append(j+str(i))
    return new_list


print("New list:", concat(my_list))
