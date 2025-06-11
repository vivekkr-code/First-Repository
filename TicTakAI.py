import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for a win condition
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_full(board):
    return all([spot != ' ' for spot in board])

# Minimax Algorithm to find the best move for the AI
def minimax(board, depth, is_maximizing, alpha, beta):
    # Check for terminal states (win or draw)
    if check_win(board, 'X'):
        return -10 + depth
    elif check_win(board, 'O'):
        return 10 - depth
    elif check_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move for AI (Player 'O')
def ai_move(board):
    best_move = -1
    best_value = float('-inf')
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_value = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    
    return best_move

# Main game loop
def play_game():
    board = [' ' for _ in range(9)]  # Board representation with empty spaces
    current_player = 'X'  # Player 1 starts with 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == 'X':
            # Player X's move
            try:
                move = int(input("Player X, choose a position (1-9): ")) - 1
                if board[move] != ' ':
                    print("That spot is already taken! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            board[move] = 'X'
        else:
            # AI (Player O)'s move
            print("AI is making its move...")
            move = ai_move(board)
            board[move] = 'O'
        
        print_board(board)

        # Check for win
        if check_win(board, 'X'):
            print("Player X wins!")
            break
        if check_win(board, 'O'):
            print("AI (Player O) wins!")
            break

        # Check for draw
        if check_full(board):
            print("It's a draw!")
            break
        
        # Switch to the next player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
