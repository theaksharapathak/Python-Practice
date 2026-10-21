#Generate Square Numbers in Range
# for i in range(1,4):
#     print(i)

def square_nos():
    l = list()

    for i in range(1,31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
square_nos()
