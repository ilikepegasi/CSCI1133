def products(target):
    count = 0
    for x in range(0, 10):
        for y in range(0, x):
            for z in range(0, y):
                if (x*y*z) == target:
                    count += 1
                    print(f'{x}*{y}*{z} is {target}')
    return count

products(48)