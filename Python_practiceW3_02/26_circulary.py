#Write a Python program to check whether two lists are circularly identical.
list1 = [1,2,3,6]
list2 = [3,6,1,2]

if len(list1)==len(list2) and any(list1[i:] + list1[:i] == list2 for i in range(len(list1))):
    print("circulary identical lists")
else:
    print("unidentical lists")
                   
