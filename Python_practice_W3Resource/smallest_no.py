#Get Smallest Number in List

def smallest_no(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest
print("Smallest no is", smallest_no([2,3,44,44,1,99]))

print("Small no is ", min([2,3,4,99,8]))