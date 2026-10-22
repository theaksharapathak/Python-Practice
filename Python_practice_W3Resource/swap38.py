#Swap Every n-th and (n+1)th Values
from itertools import chain, zip_longest
def swap(l):
    return list((chain.from_iterable(zip_longest(l[1::2], l[::2]))))

l=[0,1,2,3,4,5]
print(swap(l))
