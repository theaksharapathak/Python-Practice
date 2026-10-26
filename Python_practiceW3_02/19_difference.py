#Calculate Difference Between Lists
list1 = [1,2,3,4]
list2 = [2,3,8,9]
difference = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
print(difference)