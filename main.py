s='''
████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝'''
print(s)

board = [    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

turn = "X"

def print_board():
    print("#" * 13)
    for row in board:
        print("#" + " ".join(cell.rjust(3) for cell in row) + "#")
        print("#" + " ".join(" " * 3 for _ in range(3)) + "#")
    print("#" * 13)
def get_player_move():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid indices. Please enter a row and column between 0 and 2, inclusive.")
            continue
        if board[row][col] == "":
            board[row][col] = turn
            break
        print("That space is already occupied. Please try again.")

def check_win():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return ""

while True:
    print_board()
    get_player_move()
    winner = check_win()
    if winner:
        print(f"{winner} wins!")
        break
    if not any("" in row for row in board):
        print("It's a draw!")
    turn = "O" if turn == "X" else "X"
