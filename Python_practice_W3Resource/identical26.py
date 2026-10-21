#Check Circularly Identical Lists
list1 = [1,2,3,4]
list2 = [3,4,1,2,9]

if len(list1) == len(list2) and any(list1[i:] + list1[:i] == list2 for i in range(len(list1))):
    print("Lists are circularly identical")
else:
    print("Lists are not circularly identical")