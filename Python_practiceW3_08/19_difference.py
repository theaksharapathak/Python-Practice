l1 = [78,22,33]
l2 = [9,45,78]

difference = list(set(l1)-set(l2)) + list(set(l2)-set(l1))
print(difference)