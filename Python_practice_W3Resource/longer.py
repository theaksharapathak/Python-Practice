#Find Words Longer Than n

l = ['ok','word','mom','new','thunder','Hi','k']
n = 2
def find_words(l):
    result = []
    for item in l:
        if len(item)>n:
            result.append(item)
    return result
print("Words longer than n:", find_words(l))   