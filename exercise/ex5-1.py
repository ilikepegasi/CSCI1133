def count_by_fives(upper):
    sum = 0
    for i in range(1, (upper // 5) + 1):
        print(i * 5)
        sum += i * 5
    return sum

count_by_fives(32)