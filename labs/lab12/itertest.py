numbers1 = [0, 1, 2, 3, 4, 5]
numbers2 = [0, 1]
def iterator(iterable) -> list:
    for i in range(0, len(iterable)-1):
        for j in range(i+1, len(iterable)):
            print(i, j)
            
iterator(numbers1)
iterator(numbers2)