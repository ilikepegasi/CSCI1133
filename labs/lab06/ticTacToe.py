import random


def print_board(board):
    print(f"{board[0]}{board[1]}{board[2]}\n{board[3]}{board[4]}{board[5]}\n{board[6]}{board[7]}{board[8]}")

def open_spots(board):
    open_spot_indexes = []
    for i in range(len(board)):
        if board[i] == "-":
            open_spot_indexes.append(i)
    return open_spot_indexes

def random_move(board, symbol):
    board[random.choice(open_spots(board))] = symbol

def check_three(board, idx1, idx2, idx3):
    if board[idx1] == board[idx2] and board[idx2] == board[idx3]:
        if board[idx1] == "X":
            return "X"
        elif board[idx1] == "O":
            return "O"
    return "-"

def winner(board):
    winning_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for state in winning_states:
        row_state = check_three(board, state[0], state[1], state[2])
        if row_state == "X":
            return "X"
        elif row_state == "O":
            return "O"
    if "-" not in board:
        return "D"
    return "-"

def tic_tac_toe():
    board_state = []
    for i in range(0, 9):
        board_state.append("-")
    
    turn = True # True for X, False for O

    while winner(board_state) == "-":
        if turn:
            random_move(board_state, "X")
            turn = False
        else:
            random_move(board_state, "O")
            turn = True
        
    if winner(board_state) == "O":
        return "O"
    elif winner(board_state) == "X":
        return "X"
    else:
        return "D"

def average_winner_tic_tac_toe(iterations):
    winner_list = []
    for i in range(0, iterations):
        winner_list.append(tic_tac_toe())

    count_O = winner_list.count("O")
    count_X = winner_list.count("X")
    count_D = winner_list.count("D")
    print(f"X wins: {count_X}\n O wins: {count_O}\n D wins: {count_D}")
    total = count_O + count_X + count_D
    print(f"X wins: {count_X / total}\n O wins: {count_O / total}\n D wins: {count_D / total}")


def main():
    inputted_board = ['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O']
    print_board(inputted_board)
    print(open_spots(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O']))
    print(check_three(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'], 1, 4, 7))
    random_move(inputted_board, "O")
    print(winner(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
    print(tic_tac_toe())
    average_winner_tic_tac_toe(100000000)

if __name__ == "__main__":
    main()