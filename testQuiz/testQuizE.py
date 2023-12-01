def compute(x):                 #1
    count = 0                   #2
    if x == 0:                  #3
        return count            #4
    elif x % 2 == 0:            #5
        return 1 + compute(x-1) #6
    else:                       #7
        count += 5              #8
        return compute(x-1)
    


def deep7(collection):
    if isinstance(collection, str): #Checks if collection is a string
        return 7
    elif collection == []:
        return []
    else:
        return [deep7(collection[0])] + deep7(collection[1:])
    

def mystery(n):
    steps = 0
    while n > 0:
        if n % 3 == 0:
            n = n//3
        else:
            n = n-7
        steps += 1
    return steps

def mystery2(n):
    if not n > 0:
        return 0
    elif n % 3 == 0:
        return 1 + mystery(n // 3)
    else:
        return 1 + mystery(n-7)
    
def three(words):
    if words == []:
        return []
    if len(words[0]) == 3:
        return [words[0]] + three(words[1:])
    else:
        return three(words[1:])
    
print(three(['not', 'all', 'of', 'these', 'words', 'are', 'length', 'three']))
    