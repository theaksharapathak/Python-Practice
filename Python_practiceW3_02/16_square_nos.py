#Generate Square Numbers in Range
def square_nos():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(square_nos()[:5])
print(square_nos()[-5:])
