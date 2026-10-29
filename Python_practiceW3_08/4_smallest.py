l = [23,34,11]

def smallest_no(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_no(l))