#Sum Items in List
l = [1,2,33]

def sum_list(items):
    sum = 0
    for i in items:
        sum+= i
    return sum

print(sum_list(l))