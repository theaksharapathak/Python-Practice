#Write a Python program to get the largest number from a list.

def largest_no(items):
    n = items[0]
    for item in items:
        if item > n:
            n = item
    return n
print(largest_no([1,99,23,899]))
