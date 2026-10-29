# Get Smallest Number in List
# Write a Python program to get the smallest number from a list.
my_list = [100, 2, 33]


def smallest_no(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest


print(smallest_no(my_list))
