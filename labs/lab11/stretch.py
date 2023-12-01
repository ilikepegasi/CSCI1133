import warmup

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def double_reverse(str_list: list[str]) -> list[str]:
    if str_list == []:
        return []
    return double_reverse(str_list[1:]) + [warmup.reverse_string(str_list[0])]


if __name__ == "__main__":
    print(fibonacci(3))
    print(fibonacci(20))
    print(double_reverse(['these', 'words', 'will', 'be', 'reversed']))