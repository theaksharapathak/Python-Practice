# Sort Tuples by Last Element
# Write a Python program to get a list, sorted in increasing order
#  by the last element in each tuple from a given list of non-empty tuples.
my_list = [(1, 2), (3, 43), (23, 1), (9, 1)]


def last(n):
    return n[-1]


def sort_list(items):
    return sorted(items, key=last)


print(sort_list(my_list))
