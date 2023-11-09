def total_cost(order:dict, prices:dict):
    #TODO add docstring
    '''
    '''
    total_price = 0
    for key in order:
        total_price += prices[key] * order[key]
    return total_price

def follows(text: str):
    #TODO add docstring
    text = text.split()
    following = {}
    for word in text:
        following[word] = []
    for i, word in enumerate(text):
        if i != len(text) - 1:
            following[word].append(text[i + 1])
    print(following)
