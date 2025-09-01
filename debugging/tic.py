#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)

        # input validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # place move
        board[row][col] = player
        moves += 1

        # check winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # check draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()