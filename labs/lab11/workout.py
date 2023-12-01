def deep_square(numbers: list) -> list:
    if numbers == []:
        return []
    elif type(numbers) == list:
        return [deep_square(numbers[0])] + deep_square(numbers[1:])
    else:
        return numbers ** 2

def flatten(lst: list) -> list:
    if lst == []:
        return []
    elif type(lst) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst]

def flat_square(lst):
    return flatten(deep_square(lst))




if __name__ == "__main__":
    print(deep_square([[-1, [2], [3], [[[-4,5]]], [], []]]))
    print(deep_square([-7, [2, 5, [-3], [], [[5, 7], 1]], -7]))
    print(flatten([[-1, [2], [3], [[[-4,5]]], [], []]]))

    print(flatten([-7, [2, 5, [-3], [], [[5, 7], 1]], -7]))
    print(flat_square([[-1, [2], [3], [[[-4,5]]], [], []]]))
