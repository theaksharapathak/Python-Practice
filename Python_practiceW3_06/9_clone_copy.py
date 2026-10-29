# Clone or Copy a List
# Write a Python program to clone or copy a list.
my_list = [1, 22, 3]


def clone_list(items):
    new_list = []
    for item in items:
        new_list.append(item)
    return new_list

print(clone_list(my_list))
