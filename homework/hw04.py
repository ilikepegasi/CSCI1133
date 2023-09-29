def sound(weight):
    '''
    Purpose:
        Based on the weight of your dog, predicts how their bark will sound using onomonopeia
    Parameter(s):
        weight: the weight of your dog in pounds (float/int)
    Return Value:
        The predicted onomonapeia of your dog's bark (str)

    '''
    if(weight < 13):
        return "Yip"
    elif(weight < 30):
        return "Ruff"
    elif(weight < 70):
        return "Bark"
    else:
        return "Boof"


if __name__ == "__main__":
    
    print(sound(6)) # Should output Yip
    print(sound(31)) # Should output Bark
    print(sound(14)) # Should output Ruff
    print(sound(90)) # Should output Boof

