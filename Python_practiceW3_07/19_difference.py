#Calculate Difference Between Lists
l1 = [1,22,9]
l2 = [9,23,1]

difference = list(set(l1)-set(l2))+ list(set(l2)-set(l1))
print(difference)