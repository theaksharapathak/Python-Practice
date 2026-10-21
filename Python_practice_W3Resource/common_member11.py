#Write a Python function that takes two lists and 
# returns True if they have at least one common member.


def check_common_member(l1,l2):
    result = False

    for x in l1:
        for y in l2:
            if x == y:
                result = True
    
    return result

l1 = [1,2,3]
l2 = [0,88,9]
print(check_common_member(l1, l2))


