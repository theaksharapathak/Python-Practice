#Convert Pairs to Sorted Unique Array
# a = set([1,2,3,3,3,2,1,99,8])
# print(a)
L = [(1, 2), (3, 4), (3,4), (8,9)]
print(sorted(set().union(*L)))