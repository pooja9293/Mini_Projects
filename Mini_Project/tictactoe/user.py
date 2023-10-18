board = [" " for _ in range(9)]
def display_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def check_draw():
    return " " not in board
current_player = "X"
while True:
    display_board()
    position = int(input(f"Player {current_player}, enter a position (0-8): "))
    
    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move. Try again.")
        continue
    
    board[position] = current_player
    
    if check_win(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break
    elif check_draw():
        display_board()
        print("It's a draw!")
        break
    
    current_player = "O" if current_player == "X" else "X"
