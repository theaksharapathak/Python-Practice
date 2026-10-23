#Write a Python program to get the smallest number from a list.

def smallest_no(items):
    small_no = items[0]
    for item in items:
        if item < small_no:
            small_no = item
    return small_no
print(smallest_no([100,2,99,344,1]))