# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Melanie Rosado
# Created: 2018-11-08

symbol = [ " ", "x", "o" ]

def printRow(row):
    output = "l"
    for cell in row:
        output += " " + symbol[cell] + "  l"
    print (output)

def printBoard(board):
    board = [[0,1],
             [2,3],
             [4,5],
             [6,7]]
    for row in board:
             print (printRow)
             print (nextBorder)

def markBoard(board, row, col, player):
    1 = []
    if player == 1:
        print (1)
    if player == 2:
        print (2)
    if square != "":
        return True
    else:
        return False
 

def getPlayerMove():
    prompt = int(input("Enter the row and column number:"))
    return prompt

def hasBlanks(board):
    for row in board:
        for square in row:
            if square == " ":
                return True
    return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]       
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 

main()
