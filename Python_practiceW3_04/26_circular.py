#Check Circularly Identical Lists
#Write a Python program to check whether two lists are circularly identical.
l1 = [1,2,3,4]
l2 = [32,4,1,2]


if len(l1)==len(l2) and any(l1[i:] + l1[:i] == l2 for i in range(len(l1))):
    print("lists are circularly identical")
else:
    print("lists are not circularly identical")