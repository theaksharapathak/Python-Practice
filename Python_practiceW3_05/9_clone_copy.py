#Clone or Copy a List
#Write a Python program to clone or copy a list.
my_list = [1,2,23]
new_list = []

def clone_list(items):
    for i in items:
        new_list.append(i)
    return new_list

print("original list:", my_list)
print("new list:", clone_list(my_list))