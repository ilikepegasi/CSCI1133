import random as rand

def total_cost(order: dict, prices: dict):
    """
    Purpose:
        Returns a total cost based on the amount of orders for each item in the first
        dictionary, and the cost for each item in the second dictionary
    Parameter(s):
        order (dict{str: int}): a dictionary representing a relation between an item and its amount 
        ordered
        prices (dict{str: int}): a dictionary representing a relation between an item and its price
    Return Value (int):
        the total cost of the order based on the amount of oredrs for each item and their prices
    """
    total_price = 0
    for key in order:
        total_price += prices[key] * order[key]
    return total_price

def follows(text: str):
    """
    Purpose:
        From a string representing a sentence, creates a dictionary with keys representing
        each word  in the sentence and values being a list of the the words that follow it 
        in the sentence, excluding duplicates
    Parameter(s):
        text (str): a string representing the sentence to create the dictionary from
    Return Value (dict{str: list[str]}):
        a dictionary, with its keys being each word of the inputted sentence, and its values
        being a list of each word that follows that key word, without duplicates
    """
    text = text.split()
    following = {}
    for i, word in enumerate(text):
        if (i != len(text) - 1):
            if word in following:
                following[word].append(text[i + 1])
            else: 
                following[word] = [text[i + 1]]
    return following

def suggest(current: str, follows_dict: dict):
    """
    Purpose:
        Finds a list of words to potentially follow the inputted string based
        on the contents of the inputted dictionaty. If the inputted string is a key in
        the dictionary, it returns that key's values, which should represent
        a list of possibilities to what the next word should be. If the inputted 
        string is not a key in the dictionary, the function will return all of the 
        dictionary's keys as a list
    Parameter(s):
        current (str): a string representing the word to find a list of possible words to follow it
        follows_dict (dict{str, list[str]}): a dictionary, with its keys being words and its values
        being lists of words that can follow the key
    Return Value (list[str]):
        a list of strings representing words that can follow the inputted string
    """
    if current in follows_dict:
        return follows_dict[current]
    return list(follows_dict.keys())

def has_punctuation(word: str):
    """
    Purpose:
        Determines whether the inputted word has the punctuation . ! or ?
    Parameter(s):
        word (str): the string representing the word to determines prescence of punctuation
    Return Value (bool):
        Whether the inputted word has the punctuation . ! or ?
    """
    punctuation = ".!?"
    for letter in punctuation:
        if letter in word:
            return True
    return False

def random_sent(fname: str, max_length: int):
    """
    Purpose:
        From an inputted file and a maximum length, constructs a sentence with a rudimentary
        sentence completion algorithm, using a random choice of all the words that follow
        one word in the inputted file, starting with a randomly selected word in the file, 
        with a maximum legnth equal to the inputted integer. The sentence will also terminate
        on certain punctuation being ., !, or ?.
    Parameter(s):
        fname (str): the filepath of the inputted file that will serve as the basis for 
        the sentence completion algorithm
        max_length (int): the maximum length of the output sentence
    Return Value (str):
        The randomly generated sentence, maximum length being the inputted integer, using
        the inputted file as a, in a way, "training data" for the algorithm
    """
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read()
    following = follows(text)
    current = rand.choice(text.split())
    sentence = [current]
    while not has_punctuation(current) and len(sentence) < max_length:
        current = rand.choice(suggest(current, following))
        sentence.append(current)
    return " ".join(sentence)

if __name__ == "__main__":
    print(follows("When I do nothing"))
