l = [2,3,100]

def largest_no(items):
    largest = items[0]
    for i in items:
        if i > largest:
            largest = i
    return largest

print(largest_no(l))