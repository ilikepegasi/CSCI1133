def mystery(lst: list[int]) -> list[int]:
    '''
    A: Subtracts 5 from each element in a list
    B: An emptpy list
    C: Yes. Each call, it slices off one element of the inputted list
    '''
    if lst == []:
        return []
    else:
        return [lst[0]-5] + mystery(lst[1:])

def mystery_loop(lst: list[int]) -> list[int]:
    for i, ele in enumerate(lst):
        lst[i] -= 5
    return lst

def sum_list(vals: list[int]) -> int:
    '''
    A: An empty list
    B: Adds the first element of list list, plus the sum of the rest of the list
    C: Will add up each element of the list, removing the first element of the list, moving down to an empty list
    '''
    if vals == []:
        return 0
    return vals[0] + sum_list(vals[1:])

def reverse_string(st: str) -> str:
    if st == "":
        return ""
    return reverse_string(st[1:]) + st[0]

if __name__ == "__main__":
    print(mystery([6, 4, 23 ,7, -1]))
    print(mystery_loop([6, 4, 23 ,7, -1]))
    print(sum_list([6, 4, 23 ,7, -1]))
    print(reverse_string("Alphabet"))