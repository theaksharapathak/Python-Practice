#Write a Python program to calculate the difference between the two lists.
list1 = [1,2,3]
list2 = [4,2,6]
difference = list(set(list1)-set(list2)) + list(set(list2)-set(list1))
print(difference)
