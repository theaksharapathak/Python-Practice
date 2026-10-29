#Calculate Difference Between Lists
#Write a Python program to calculate the difference between 
# the two lists.
l1 = [1,22,34]
l2 = [35,22,1]

difference = list(set(l1)-set(l2)) + list(set(l2)-set(l1))
print(difference)