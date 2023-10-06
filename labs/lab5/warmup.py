def div27(num):
    out = False
    for i in range(2,8):
        if num % i == 0:
            out = True
    out = False
    return out

if __name__ == '__main__':
    print(div27(15)) #Should return True
