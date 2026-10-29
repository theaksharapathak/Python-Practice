#Write a Python program to create a list by concatenating a given 
# list with a range from 1 to n.
my_list = ['cat','cake','momos']


def concat(items):
    new_list = []
    for i in range(1, 3):
        for j in items:
            new_list.append(j + str(i))
    return new_list

print(concat(my_list))
