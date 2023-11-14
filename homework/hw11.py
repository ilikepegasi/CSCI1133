def collatz(n: int) -> int:
    #TODO add docstring
    seq_len = 0
    if n == 1:
        return seq_len + 1
    elif n % 2 == 1:
        return seq_len + collatz(n * 3 + 1) + 1
    else:
        return seq_len + collatz(n // 2) + 1

def all_names(first_names, last_names, length):
    