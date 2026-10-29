#Sum Items in List
my_list = [1,2,33]

def sum_list():
    total = 0
    for i in my_list:
        total+= i
    return total

print(sum_list())