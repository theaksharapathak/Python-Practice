#Calculate Difference Between Lists
list1 = [1,2,3,499,98]
list2 = [8,9,2,3,99]

difference = list(set(list1)-set(list2)) + list(set(list2)-set(list1))
print(difference)