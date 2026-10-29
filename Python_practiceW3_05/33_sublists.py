#Generate All Sublists
#Write a Python program to generate all sublists of a list.
l = [1,2,33]
sublists = []

for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        sublists.append(l[i:j])

print(sublists)
                   