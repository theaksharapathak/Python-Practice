l = [1,22,45]
sublists = []

for i in range(len(l)):
    for j in range(i+1, len(l)+1):
        sublists.append(l[i:j])

print(sublists)