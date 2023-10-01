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
    choice = input("Choose A, B, or C: ")
    while((choice != "A") and (choice != "B") and (choice != "C")):
        print("Invalid option, try again.")
        choice = input("Choose A, B, or C: ")
    return choice

def adventure():
    '''
    Purpose:
        Prompts the user to choose a series of actions based on prompts to complete a textual adventure, with a binary good or bad ending based on those choices
    Parameter(s):
        None
    Return Value:
        Whether your adventure ending good or badly based on your choices (bool)
    '''
    prompt1 = "Intense lightning strikes down from above. Your old mentor looks upon you. You never thought he would do this, but now you are falling towards the windswept rocks below. You need to stop yourself from crashing down, but how? "
    option1a = "Remember your allies, the friends you made along the way. Call for the noble Daisy to save you, with your golden whistle."
    option1b = "You know there is still some good in him. Reach out to your mentor and ask him to remember"
    option1c = "Call upon your deep wellspring of magical power and will yourself back onto the top of the cliff."
    choice1 = three_options(prompt1, option1a, option1b, option1c)
    print(choice1)

    if(choice1 == "A"):
        print("The puppy you raised from birth, now your noble flying daschund Daisy, swoops down to save your hide just before you are dashed on the rocks. You let a tear fall for your mentor before flying away.")
        return True
    elif(choice1 == "B"):
        print("His face is pushed away, as if by some unseen force, but something comes over his face. He tosses a rope down to you and you climb back up. But as you look to him, he scowls. The moment has passed.")
        flag2 = True
        flag3 = False
        flag4 = False
    else:
        print("Your magic is nearly emptied after your long trek to the cliffs, but you manage to push through, and you are returned to the cliff you just were pushed off of- by a the man who still stands there.")
        flag2 = False
        flag3 = False
        flag4 = True

    if flag2:
        prompt2 = "He helped you up... But will he keep helping you? Will you trust him, or take this oppurtunity to end his threat?"
        option2a = "He still has good in him, he showed that. Reach out a hand in kindness."
        option2b = "In his moment of weakness, now you can push him off the cliff."
        option2c = "You need to run, get far away from this place and warn the others."
        choice2 = three_options(prompt2, option2a, option2b, option2c)
    else:
        choice2 = 0
    
    if(choice2 == "A"):
        print("He shakes his head, and you see him breathe in a deep maroon smoke. \"No, I am too far gone. Leave me behind.\"")
        flag3 = True
        flag4 = False
    elif(choice2 == "B"):
        print("\"You really thought that would work?\" he says, chuckling. He turns away, and you are enveloped in a dark smoke as you are transported to the realm of fire.")
        return False
    elif(choice2 == "C"):
        print("You only get so far before your mentor's honor guard intercepts you and your quest has a unsatisfactory end.")
        return False
    
    if flag3:
        prompt3 = "You can see your words are getting through to him- but there is some outside force controlling him. You need to stop it."
        option3a = "The only way this ends is with your mentor put out of his misery. Wield the Sword of Evening and stab him through."
        option3b = "Your magical power may be able to purify him. Reach out to him and channel the Light of Eternity through his soul."
        option3c = "Pull him into a hug."
        choice3 = three_options(prompt3, option3a, option3b, option3c)
    else:
        choice3 = 0

    if(choice3 == "A"):
        print("As you draw the sword, he chuckles. You feel the swords power over shadows bend to him, and he now wields it to end you.")
        return False
    elif(choice3 == "B"):
        print("You feel a prescence thought to be long gone from the face of the planet as you are blasted away from your mentor.")
        flag4 = True
    elif(choice3 == "C"):
        print("Hugs always work.")
        return True

    if flag4:
        prompt4 = "He looks upon you and says \"Oh, child. You were always so powerful. But it's too late. I am under the power of the Dark One.\""
        option4a = "Calling upon your friendship with Our Lady of Light, and Daisy, and Adora, and you get the idea, cleanse that vile influence from his soul."
        option4b = "Pledge your allegiance to the Dark One and rule together."
        option4c = "Use this moment of weakness to end the threat of the Dark One."
    else:
        choice4 = 0

    if(choice4 == "A"):
        print("You have saved your mentor from the influence of the Dark One, but they are still out there. But you have an old friend at your side once more.")
        return True
    elif(choice4 == "B"):
        print("I guess that counts as a win????")
        return True
    elif(choice4 == "C"):
        print("The Dark One's paranoid mind saw that one coming. You are deflected off the edge of the cliff once more, this time to your doom.")
        return False
    
    return False


if __name__ == "__main__":
    
    print(sound(6)) # Should output Yip
    print(sound(31)) # Should output Bark
    print(sound(14)) # Should output Ruff
    print(sound(90)) # Should output Boof


if __name__ == '__main__':
    print(sound2(13, True)) # Should output Meow
    print(sound2(50, False)) # Should output Bark
    print(sound2(14, True)) # Should output Meow
    print(sound2(90, False)) # Should output Boof

if __name__ == '__main__':
    print(adventure())