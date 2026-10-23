#Sort Tuples by Last Element
def last(n):
    return n[-1]
# print(last((2,3)))

def sort(tupples):
    return sorted(tupples, key=last)

t = ((2,3),(4,9),(9,0))
print(sort(t))

