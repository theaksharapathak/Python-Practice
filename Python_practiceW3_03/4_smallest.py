#Write a Python program to get the smallest number from a list.
my_list = [100,2,99,77,1]

def smallest_no(items):
    smallest = items[0]
    for item in items:
        if item < smallest:
            smallest = item 
    return smallest

print("Smallest no :", smallest_no(my_list))
