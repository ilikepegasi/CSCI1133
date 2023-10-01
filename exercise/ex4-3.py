def largest():
    userNum = [int(input("Enter a number: "))]
    i = 0
    while userNum[i] != 0:
        i += 1
        userNum.append(int(input("Enter a number: ")))
    return max(userNum)


