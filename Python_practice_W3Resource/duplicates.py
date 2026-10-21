#Remove Duplicates from List

def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)

    return result
list = [1,2,2,3,3,1,4,5,99,99]
print("List w/o duplicates = ", remove_duplicates(list))