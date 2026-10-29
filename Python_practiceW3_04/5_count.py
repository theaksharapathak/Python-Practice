# Count Strings with Same Start and End
# Write a Python program to count the number of strings from
# a given list of strings. The string length is 2 or more and
# the first and last characters are the same.
my_list = ['wow', 'mom', 'cat']


def count_fn(items):
    count = 0
    for i in items:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count


print("total no:", count_fn(my_list))
