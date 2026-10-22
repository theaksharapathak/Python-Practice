#Create List with Range Concatenation
my_list = ['p','q']
n=4
new_list = []
for i in range(1,n+1):
    for j in my_list:
        new_list.append(j+str(i))
print(new_list)