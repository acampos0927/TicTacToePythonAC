# Tic-Tac-Toe Game in Python

# Print the game board
def print_board(board):
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---|---|---")

# Check if a player has won
def check_win(board, player):
    for i in range(3):
        # Check rows and columns
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Check if the board is full
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get valid player input for row and column
        row, col = -1, -1
        while row not in [0, 1, 2] or col not in [0, 1, 2] or board[row][col] != " ":
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
            except ValueError:
                continue
        
        # Place the move
        board[row][col] = current_player
        
        # Check if the current player won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
