#Write a Python program to get a list, sorted in
#  increasing order by the last element in each tuple from 
# a given list of non-empty tuples.
my_list = [(1,290),(3,4),(2,99),(1,100)]

def last(n):
    return n[-1]
def sort_list(items):
    return sorted(items, key=last)

print(sort_list(my_list))