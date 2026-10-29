#Check Circularly Identical Lists
#Write a Python program to check whether two lists are circularly identical.
list1 = [1,22,98]
list2 = [98,1,2]

if len(list1)==len(list2) and any(list1[i:] + list1[:i] for i in range(len(list1))):
    print("lists are circularly identical")
else:
    print("not identical")