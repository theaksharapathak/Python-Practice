#Get Smallest Number in List
my_list = [100,22,3]

def smallest_no(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_no(my_list))