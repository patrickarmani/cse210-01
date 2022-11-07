"""
file: tictactoes.py
author: Patrick Armani
CSE 210 - 2022

"""
import random

board = ["_","_","_",
        "_","_","_",
        "_","_","_"]

currentPlayer = "X"
winner = None
gameRunning = True
# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
# take player input
def playerInput(board):
    numberType = int(input("Choose a number from 1 to 9: "))
    if numberType >= 1 and numberType <= 9 and board[numberType-1] == "_" :
        board[numberType-1] = currentPlayer
    else:
        print("This player is already in that spot!")
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
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
        
def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

# computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "0"
            switchPlayer()
        
    
    
# check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)