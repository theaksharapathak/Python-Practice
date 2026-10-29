l = [1,22,3]


def clone_list(items):
    new_list = []
    for i in items:
        new_list.append(i)
    return new_list

print(clone_list(l))