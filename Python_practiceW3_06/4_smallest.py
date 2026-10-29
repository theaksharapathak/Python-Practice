#Get Smallest Number in List
#Write a Python program to get the smallest number from a list.
l = [22,300,3]

def smallest_no(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_no(l))