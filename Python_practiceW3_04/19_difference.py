#Calculate Difference Between Lists
#Write a Python program to calculate the difference between the two lists.
l1 = [2,3,44]
l2 = [44,3,11]


difference = list(set(l1)-set(l2)) + list(set(l2)-set(l1))
print(difference) 