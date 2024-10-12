from days.day_083.files.helpers import *


def day_083():
    title("TIC TAC TOE")

    def print_board(board):
        print("\n  1   2   3")  # column headers
        for i, row in enumerate(board):
            print(f"{i + 1} " + " | ".join(row))  # row headers
            if i < 2:
                print("  ---------")  # Row separators for clarity

    def check_win(board, player):
        # Check rows
        for row in board:
            if all(s == player for s in row):
                return True
        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(
            board[i][2 - i] == player for i in range(3)
        ):
            return True
        return False

    def check_draw(board):
        return all(board[row][col] != " " for row in range(3) for col in range(3))

    def tic_tac_toe():
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)
            move = input(
                f"Player {current_player}, enter your move (format: row,col) (nums: 1-3): "
            )

            try:
                row, col = map(int, move.split(","))
            except ValueError:
                print("Invalid input format. Please enter row and column as 'row,col'.")
                continue

            if row not in range(1, 4) or col not in range(1, 4):
                print("Invalid row or column. Please enter values between 1 and 3.")
                continue

            # Convert 1-based input to 0-based indexing for internal representation
            row -= 1
            col -= 1

            if board[row][col] != " ":
                print("Cell already taken, choose another one.")
                continue

            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

    tic_tac_toe()
