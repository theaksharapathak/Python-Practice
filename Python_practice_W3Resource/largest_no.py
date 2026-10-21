#Get Largest Number in List

def largest_no(items):
    largest = items[0]
    for item in items:
        if item > largest:
            largest = item
    return largest
print("Largest No =", largest_no([23,20,29,999]))