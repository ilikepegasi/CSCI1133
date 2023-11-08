def total_cost(order:dict, prices:dict):
    #TODO add docstring
    '''
    '''
    total_price = 0
    for key in order:
        total_price += prices[key] * order[key]
    return total_price

def follows(text: string):
    print()