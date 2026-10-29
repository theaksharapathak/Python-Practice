# Get Largest Number in List
#Write a Python program to get the largest number from a list.

my_list = [1,2,34]

def largest_no(items):
    largest = items[0]
    for i in items:
        if i > largest:
            largest = i
    return largest

print(largest_no(my_list))