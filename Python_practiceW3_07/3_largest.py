#Get Largest Number in List
my_list = [1,22,100]

def largest_no(items):
    largest = items[0]
    for i in items:
        if i > largest:
            largest=i
    return largest

print(largest_no(my_list))