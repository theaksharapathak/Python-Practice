# Sum all the items in a list

def sum_list(items):
    sum_nos = 0
    for item in items:
        sum_nos += item
    return sum_nos
print(sum_list([10,10,10]))