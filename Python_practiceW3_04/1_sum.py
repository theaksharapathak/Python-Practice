#Write a Python program to sum all the items in a list.
my_list = [1,2,3]


def sum_fn(items):
    sum_list = 0
    for i in items:
        sum_list += i
    return sum_list

print("total:", sum_fn(my_list))