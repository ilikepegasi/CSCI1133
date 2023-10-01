def sound(weight):
    '''
    Purpose:
        Based on the weight of your dog, predicts how their bark will sound using onomonapeia
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

def sound2(weight, is_cat):
    '''
    Purpose:
        Based on whether your pet is a cat and its weight, predicts what their sound will be using onomonapeia
    Parameter(s):
        weight: the weight of your pet in pounds (float/int)
        is_cat: whether your pet is a cat (bool)
    Return Value:
        The predicted onomonapeia of your pet's sound (str)
    '''

    if is_cat != True:
        return sound(weight)
    else:
        return "Meow"

def three_options(text, optionA, optionB, optionC):
    '''
    Purpose:
        Prompts the user to choose between three options and then returns that choice
    Parameters:
        text: the text prompt for the user's choice (str)
        optionA: the first textual choice for the user, correlating to A return value (str)
        optionB: the second textual choice for the user, correlating to B return value (str)
        optionC: the third textual choice for the user, correlating to C return value (str)
    Return Value:
        The chosen option from the user (str)
    '''
    print(text)
    print(f"A: {optionA}")
    print(f"B: {optionB}")
    print(f"C: {optionC}")
    choice = input("Choose A, B, or C")
    while((choice != "A") and (choice != "B") and (choice != "C")):
        print("Invalid option, try again.")
        choice = input("Choose A, B, or C")
    return choice

if __name__ == "__main__":
    
    print(sound(6)) # Should output Yip
    print(sound(31)) # Should output Bark
    print(sound(14)) # Should output Ruff
    print(sound(90)) # Should output Boof


if __name__ == '__main__':
    print(sound2(13, True)) # Should output Meow
    print(sound2(50, False)) # Should output Bark
    print(sound2(14, True)) # Should output Ruff
    print(sound2(90, False)) # Should output Boof
