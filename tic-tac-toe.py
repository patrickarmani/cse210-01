'''
File: tic-tac-toe.py
Author: Patrick Armani
'''
currentPlayer = "X"
winner = None
gameRunning = True
def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 
    
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# printing the game board
def display_board(board):
    
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('_|_|_')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('_|_|_')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def is_a_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 

# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board [0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[0]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[0]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "_" not in board:
        display_board(board)
        print("It is a tie!")
        gameRunning = False

def has_winner(board):
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner} ")
        
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"
    
def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player
   

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"
    

    
if __name__ == "__main__":
    main()