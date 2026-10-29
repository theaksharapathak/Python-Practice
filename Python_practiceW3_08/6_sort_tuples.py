#Write a Python program to get a list, sorted in increasing order 
# by the last element in
#  each tuple from a given list of non-empty tuples.

l = [(1,23),(8,9),(34,2)]

def last(n):
    return n[-1]

def sort_list(items):
    return sorted(items, key=last)

print(sort_list(l))