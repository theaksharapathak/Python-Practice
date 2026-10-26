#Clone or Copy a List
my_list = [1,2,3]

def copy_list(items):
    copied_list = []
    for item in items:
        copied_list.append(item)
    return copied_list
print("original list:", my_list)
print("copied list:", copy_list(my_list))