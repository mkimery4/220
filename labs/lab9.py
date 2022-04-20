"""
Name: Margaret Kimery
<tictactoe()>.py
file: lab9.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

def tic_tac_toe():
    make_board = build_board()
    continue_playing = True
    while continue_playing:
        play(make_board)
        ans = input("Would you like to keep playing? ")
        if ans.startswith("y"):
            make_board = build_board()
            continue_playing = True
        else:
            continue_playing = False


def build_board():
  num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  return num


def fill_spot(board, position, shape):
    board[position-1] = shape


def is_legal(board, position):
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False


def game_is_won(board):
    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6]:
            return True
    for i in range(3):
        if board[i*3] == board[(i*3)+1] and board[i] == board[(i*3)+2]:
            return True

    if board[0] == board[4] and board[4] == board[8]:
        return True
    if board[2] == board[4] and board[4] == board[6]:
        return True

    else:
        return False


def game_over(board):
    if game_is_won(board):
        return True
    non_numeric = 0
    for i in board:
        if not str(i).isnumeric():
            non_numeric =+ 1
    if non_numeric == 9:
        return True
    else:
        return False


def get_winner(board):
    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6] and board[i] == "x":
            return "x"
    for i in range(3):
        if board[i*3] == board[(i*3)+1] and board[i] == board[(i*3)+2] and board[i] == "x":
            return "x"

    if board[0] == board[4] and board[4] == board[8] and board[0] == "x":
        return "x"
    if board[2] == board[4] and board[4] == board[6] and board[2] == "x":
        return "x"

    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6] and board[i] == "o":
            return "o"
    for i in range(3):
        if board[i*3] == board[(i*3)+1] and board[i] == board[(i*3)+2] and board[i] == "o":
            return "o"

    if board[0] == board[4] and board[4] == board[8] and board[0] == "o":
        return "o"
    if board[2] == board[4] and board[4] == board[6] and board[2] == "o":
        return "o"

    if not game_is_won(board):
        return "None"



def play(board):
    x_turn = True
    while not game_is_won(board):
        print_board(board)
        if x_turn:
            pos = eval(input("x's, choose a position"))
        if not x_turn:
            pos = eval(input("o's, choose a position"))
        if is_legal(board, pos):
            if x_turn:
                fill_spot(board,pos,"x")
            else:
                fill_spot(board, pos, "o")
            x_turn = not x_turn
    winner = get_winner(board)
    if winner == "x":
        print("x's win!")
    if winner == "o":
        print("o's wins!")
    if winner == "none":
        print("tie")



def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


if __name__ == '__main__':
    main()
