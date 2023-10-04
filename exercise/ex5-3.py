

def count_primes(start, stop):
    count = 0
    num = start
    while num <= stop:
        prime = True
        div = 2
        while div < num:
            if num % div == 0:
                prime = False
            div += 1
        if prime:
            print(num, "is prime")
            count += 1
        num += 1
    return count