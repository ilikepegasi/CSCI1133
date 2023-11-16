def collatz(n: int) -> int:
    #TODO add docstring
    if n == 1:
        return 1
    elif n % 2 == 1:
        return collatz(n * 3 + 1) + 1
    else:
        return collatz(n // 2) + 1

def all_names(first_names: list[str], last_names: list[str], length: int) -> list[str]:
    if first_names == []:
        return []
    first_name = first_names[0]
    return inner_names(first_name, last_names, length) + all_names(first_names[1:], last_names, length)

def inner_names(first_name: str, last_names: list[str], length: int) -> list[str]:
    if last_names == []:
        return []
    possiblity = f'{first_name} {last_names[0]}'
    if len(possiblity) == length:
        return [possiblity] + inner_names(first_name, last_names[1:], length)
    return inner_names(first_name, last_names[1:], length)

def baking_contest(time_left: int, pastries: list[list[str, int, int]]) -> int:
    points = 0
    if time_left < min_time(pastries):
        return 0
    if time_left - pastries[0][1] > 0:
        points += pastries[0][2]
        time_left -= pastries[0][1]
        return points + baking_contest(time_left, pastries[1:])
    return 0

def min_time(pastries: list[list[str, int, int]]) -> int:
    if len(pastries) == 1:
        return pastries[0][1]
    if pastries[0][1] < min_time(pastries[1:]):
        return pastries[0][1]
    return min_time(pastries[1:])

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

