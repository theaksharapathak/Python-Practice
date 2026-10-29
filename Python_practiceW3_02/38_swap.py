#Write a Python program to change the position of every
#  n-th value to the (n+1)th in a list.
l = [1,2,34,45,98,56]


for i in range(0, len(l)-1, 2):
    l[i], l[i+1] = l[i+1], l[i]

print(l)