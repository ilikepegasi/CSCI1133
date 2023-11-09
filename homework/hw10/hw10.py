import random as rand

def total_cost(order: dict, prices: dict):
    """
    Purpose:
    Parameter(s):
    Return Value:
    """
    total_price = 0
    for key in order:
        total_price += prices[key] * order[key]
    return total_price

def follows(text: str):
    """
    Purpose:
    Parameter(s):
    Return Value:
    """
    #TODO add docstring
    text = text.split()
    following = {}
    for word in text:
        following[word] = []
    for i, word in enumerate(text):
        if (i != len(text) - 1) and (text[i + 1] not in following[word]):
            following[word].append(text[i + 1])
    return following

def suggest(current: str, follows_dict: dict):
    """
    Purpose:
    Parameter(s):
    Return Value:
    """
    #TODO add docstring
    if current in follows_dict:
        return follows_dict[current]
    return list(follows_dict.keys())

def has_punctuation(word:str):
    #TODO add docstring
    punctuation = ".!?"
    for letter in punctuation:
        if letter in word:
            return True
    return False

def random_sent(fname:str, max_length:int):
    """
    Purpose:
    Parameter(s):
    Return Value:
    """
    #TODO add docstring
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read()
    following = follows(text)
    current = rand.choice(text.split())
    sentence = [current]
    while not has_punctuation(current) and len(sentence) < max_length:
        current = rand.choice(suggest(current, following))
        sentence.append(current)
    return " ".join(sentence)