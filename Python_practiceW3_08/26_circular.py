l1 = [1,22,34]
l2 = [22,34,1]

if len(l1)== len(l2) and any(l1[i:] + l1[:i] == l2 for i in range(len(l1))):
    print("circular")

else:
    print("not circular")