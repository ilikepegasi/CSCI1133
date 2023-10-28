def do_things2(i, j):
    prod = 1
    x = 70
    while x < j:
        if ((x % i) == 0):
            prod *= (7 + x)
        else:
            print(x, "b")
        x += 1
    return prod

def do_things(i, j):
    prod = 1
    for x in range(70, j):
        if (x % i) == 0:
            prod *= (7+x)
        else:
            print(x, "a")
    return prod

def test1(word):
    for x in word:
        print(x)

def test2(word):
    for y in range(0, len(word)):
        print(word[y])

def get_value(ch):                #1
    for digit in '1234567890':     #2
        if ch == digit:             #3
            return int(ch)         #4
    return 0                       #5

entry = input("Message: ")        #6
total = 0                          #7
idx = 0                            #8
while idx < len(entry):            #9
    total += get_value(entry[idx]) #10
    idx += 1                        #11
print("Total is:", total)          #12

