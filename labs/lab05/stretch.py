def mul(a, b):
    res = 0
    for i in range(0, b):
        res += a
    return res

def mul2(a, b):
    res = 0
    i = 0
    while i < b:
        res += a
        i += 1
    return res


def expo(x,y):
    prod = 1
    for i in range(0, y):
        total = 0
        for j in range(0, x):
            total += prod
        prod = total
    return prod


def expo2(x,y):
    prod = 1
    i = 0
    while i < y:
        total = 0
        j = 0
        while j < x:
            total += prod
            j += 1
        prod = total
        i += 1
    return prod


if __name__ == "__main__":
    print(mul(3, 5))
    print(mul2(2, 2))
    print(expo(2, 3))
    print(expo2(2, 3))