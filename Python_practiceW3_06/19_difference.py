#Calculate Difference Between Lists
#Write a Python program to calculate the difference between the two lists.
list1 = [1,22,98]
list2 = [98,3,4]

difference = list(set(list1)-set(list2)) + list(set(list2)-set(list1))
print(difference)