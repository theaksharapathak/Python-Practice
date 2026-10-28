#Write a Python program to check whether two lists are circularly identical.
list1 = [1,2,3,4]
list2 = [3,4,1,2]

if len(list1)==len(list2) and any(list1[2:] + list1[:2] == list2 for i in range(len(list1))):
    print("lists are identical")
else:
    print("lists are not identical")
