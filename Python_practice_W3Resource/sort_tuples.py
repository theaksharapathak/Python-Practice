#Sort Tuples by Last Element
# def last(n):
#     return n[-1]

# print(last((92,3)))

def last(n):
    return n[-1]
def sorted_tuple(tuples):
    #return sorted(tuples, key=last)
    return sorted(tuples)
print(sorted_tuple([(2,3),(9,0),(2,4)]))