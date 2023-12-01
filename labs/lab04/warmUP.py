def letters(digit):
    if digit in [1, 2, 6]:
        return 3
    elif digit in [4, 5, 9]:
        return 4
    else:
        return 5
def most_letters(numA, numB, numC):
    lenA = letters(numA)
    lenB = letters(numB)
    lenC = letters(numC)


    if (lenA == lenB) and (lenB == lenC):
        print("Tie!")
        return(0)
    elif (lenA > lenB) and (lenA > lenC):
        return(numA)
    elif (lenB > lenA) and (lenB > lenC):
        return(numB)
    elif (lenC > lenB) and (lenC > lenA):
        return(numC)
    
      

if __name__ == '__main__':
    """ print(letters(2)) #Should output 3
    print(letters(7)) #Should output 5
    print(letters(5)) """
    print(most_letters(9, 8, 5)) #Should output 8
    print(most_letters(7, 7, 7)) #Should output Tie!, followed by 0
    print(most_letters(8, 9, 5)) #Should output 8
    print(most_letters(5, 9, 8)) #Should output 8 """


