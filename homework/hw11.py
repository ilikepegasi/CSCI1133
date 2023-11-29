def collatz(n: int) -> int:
    '''
    Purpose:
        Finds the number the iterations it takes for the collatz sequence takes to finish,
        starting with an inputted number
    Parameter(s):
        n (int): The first number in the collatz sequence to complete
    Return Value (int):
        The number of iterations it took for the sequence to finish
    '''
    if n == 1:
        return 1
    elif n % 2 == 1:
        return collatz(n * 3 + 1) + 1
    else:
        return collatz(n // 2) + 1

def all_names(first_names: list[str], last_names: list[str], length: int) -> list[str]:
    '''
    Purpose: 
        Finds all combinations of two inputted lists of strings that have a 
        length equivalent to an inputted length value
    Parameter(s):
        first_names (list[str]): the list of possible first names
        last_names (list[str]): the list of possible last names
        length (int): the desired length for the strings in the returned list
    Return Value (list[str]):
        A list of all the strings from the possible combinations of input values with length 
        equivalent to the inputted length value
    '''
    if first_names == []:
        return []
    first_name = first_names[0]
    return inner_names(first_name, last_names, length) + all_names(first_names[1:], last_names, length)

def inner_names(first_name: str, last_names: list[str], length: int) -> list[str]:
    '''
    Purpose: 
        Finds all combinations of one inputted lists of strings and a single string that have a
        length equivalent to an inputted length value
    Parameter(s):
        first_names (str): a possible first name
        last_names (list[str]): the list of possible last names
        length (int): the desired length for the strings in the returned list
    Return Value (list[str]):
        A list of all the strings from the possible combinations of input values with length 
        equivalent to the inputted length value
    '''
    if last_names == []:
        return []
    possiblity = f'{first_name} {last_names[0]}'
    if len(possiblity) == length:
        return [possiblity] + inner_names(first_name, last_names[1:], length)
    return inner_names(first_name, last_names[1:], length)

def baking_contest(time_left: int, pastries: list) -> int:
    '''
    Purpose:
        From an inputted set of pastries with a point value and a time, along with a time left,
        finds the maximum amount of points possible to receive by baking pastries, each taking a 
        certain amount of time and awarding a certain amount of points
    Parameter(s):
        time_left (int): the amount of time left
        pastries (list): a list containting a matrix representing the pastries, with the first element of 
        each list being its name, the second being the time to bake, and the third being point value
    Return Value (int):
        The maximum amount of points to be able to receive
    '''
    if pastries == []:
        return 0
    do_not_bake_points = baking_contest(time_left, pastries[1:])
    bake_points = pastries[0][2] + baking_contest(time_left - pastries[0][1], pastries[1:])
    if pastries[0][1] > time_left:
        return do_not_bake_points
    if do_not_bake_points < bake_points:
        return bake_points
    return do_not_bake_points
    


if False:
    #Should output ['Alex Le']
    print(all_names(['Alex', 'Rachel'], ['Le', 'Reich'], 7))

    #Should output ['Emmet Carlson', 'Emilie Nemitz']
    print(all_names(['Jack', 'Emmet', 'Emilie', 'Gayathri'],
                    ['Nemitz', 'Carlson', 'Hoversten'], 13))

    #Should output []
    print(all_names(['Nikki', 'Matthew'],
                    ['Ortiz', 'Gollamudi', 'Schoenzeit'], 14))

    #Should output ['Henry Bazell', 'Jedell Udupa', 'Rachita Omar']
    print(all_names(['Henry', 'Jedell', 'Rachita', 'Ibraheem'],
                    ['Omar', 'Udupa', 'Bazell', 'Gajjela'], 12))


if __name__ == '__main__':
    #Should output 50 (real way) or 100 (easy way)
    #Gujiya + Taiyaki
    print(baking_contest(92, [['Gujiya', 55, 30],
                    ['Taiyaki', 35, 20],
                    ['Conejito', 60, 40],
                    ['Apple Strudel', 40, 10]]))

    #Should output 40 (real way) or 100 (easy way)
    #Conejito
    print(baking_contest(76, [['Gujiya', 55, 30],
                    ['Taiyaki', 35, 20],
                    ['Conejito', 60, 40],
                    ['Apple Strudel', 40, 10]]))  

    #Should output 88 (real way) or 142 (easy way)
    #Beaver Tail + Makmur + Pionono + Sfenj
    print(baking_contest(147, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))

    #Should output 142 (real way) or 142 (easy way)
    #Enough time to get every pastry
    print(baking_contest(300, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))

    #Should output 0 (real way) or 142 (easy way)
    #Not enough time for any pastries
    print(baking_contest(21, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))

