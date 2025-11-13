# Guillermo Montiel             10-27-2025
# Assignment #4 - Four In Sequence!
# This is a playable Connect Four variant (7x6). One- or two-player modes.
# Players drop pieces by column; first to connect four horizontally, vertically,
# or diagonally wins. Shows menu, prints instructions, and loops rounds.
# CITATION: Much of the code in this assignment is heavily modified/ adapted from
# code originally created by ChatGPT
# CITATION: ACCESSED: 3-15-2023
# CITATION: URL: https://chat.openai.com

import random
import sys

def printTitleMaterial():
    print("Four In Sequence!")
    print()
    print("By: Guillermo Montiel")
    print("[COM S 127 1]")
    print()

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers != 1 and numPlayers != 2:
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber):
    if playerNumber == 0:
        return "."
    elif playerNumber == 1:
        return "X"
    elif playerNumber == 2:
        return "O"

def createBoard(width, height):
    empty = getPlayerPiece(0)
    board = []
    for i in range(height):
        board.append([])
        for j in range(width):
            board[i].append(empty)
    return board

def printBoard(board):
    for row in board:
        for column in row:
            print(column, end="")
        print()
    for i in range(len(board[0])):
        print(i, end="")
    print()
    print()

def getColumnInt(board, playerNumber):
    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))

def getInputInRange(board, playerNumber):
    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col

def getHumanInput(board, playerNumber):
    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col

def checkForNextMoveWin(board, playerNumber):
    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)
    for col in range(len(board[0])):
        row = getOpenRow(board, col)
        if row != -1:
            placePiece(board, row, col, piece)
            if checkWinner(board, playerNumber):
                placePiece(board, row, col, empty)
                return col
            placePiece(board, row, col, empty)
    return -1

def checkAdjacent(board, playerNumber):
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []
    for column in range(len(board[0])):
        row = getOpenRow(board, column)
        if row != -1:
            if row - 1 >= 0 and column - 1 >= 0 and board[row-1][column-1] == piece:
                adjacents.append(column)
            if column - 1 >= 0 and board[row][column-1] == piece:
                adjacents.append(column)
            if row + 1 < len(board) and column - 1 >= 0 and board[row+1][column-1] == piece:
                adjacents.append(column)
            if row + 1 < len(board) and board[row+1][column] == piece:
                adjacents.append(column)
            if row + 1 < len(board) and column + 1 < len(board[0]) and board[row+1][column+1] == piece:
                adjacents.append(column)
            if column + 1 < len(board[0]) and board[row][column+1] == piece:
                adjacents.append(column)
            if row - 1 >= 0 and column + 1 < len(board[0]) and board[row-1][column+1] == piece:
                adjacents.append(column)
    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]
    return col

def getComputerInput(board, currentPlayerTurn):
    opponentPlayerTurn = switchTurns(currentPlayerTurn)
    col = checkForNextMoveWin(board, currentPlayerTurn)
    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)
    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)
    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))
    print("Player {0}, please select a column between (0-{1}): {2}".format(currentPlayerTurn, len(board[0]) - 1, col))
    return col

def getOpenRow(board, col):
    empty = getPlayerPiece(0)
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == empty:
            return row
    return -1

def placePiece(board, row, col, piece):
    board[row][col] = piece

def dropPieceIntoBoard(board, col, playerNumber):
    row = getOpenRow(board, col)
    placePiece(board, row, col, getPlayerPiece(playerNumber))

def checkDraw(board):
    empty = getPlayerPiece(0)
    for row in board:
        for cell in row:
            if cell == empty:
                return False
    return True

def checkWinner(board, playerNumber):
    piece = getPlayerPiece(playerNumber)
    for row in range(len(board)):
        for column in range(len(board[0]) - 3):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True
    for row in range(len(board) - 3):
        for column in range(len(board[0])):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True
    for row in range(len(board) - 3):
        for column in range(len(board[0]) - 3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True
    for row in range(3, len(board)):
        for column in range(len(board[0]) - 3):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True
    return False

def resetGameOptions():
    currentPlayerTurn = 1
    winner = False
    draw = False
    return currentPlayerTurn, winner, draw

def switchTurns(currentPlayerTurn):
    return ((currentPlayerTurn % 2) + 1)

def main():
    running = True
    currentPlayerTurn = 1
    winner = False
    draw = False
    printTitleMaterial()
    while running:
        choice = initialChoice()
        if choice == "p":
            currentPlayerTurn, winner, draw = resetGameOptions()
            numPlayers = chooseNumPlayers()
            board = createBoard(7, 6)
            printBanner()
            printBoard(board)
            while True:
                if numPlayers == 1:
                    if currentPlayerTurn == 1:
                        col = getHumanInput(board, currentPlayerTurn)
                    elif currentPlayerTurn == 2:
                        col = getComputerInput(board, currentPlayerTurn)
                    else:
                        print("ERROR: currentPlayerTurn invalid:", currentPlayerTurn)
                        sys.exit()
                elif numPlayers == 2:
                    col = getHumanInput(board, currentPlayerTurn)
                else:
                    print("ERROR: numPlayers invalid:", numPlayers)
                    sys.exit()
                dropPieceIntoBoard(board, col, currentPlayerTurn)
                printBoard(board)
                winner = checkWinner(board, currentPlayerTurn)
                draw = checkDraw(board)
                if winner:
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    break
                elif draw:
                    print("~~ Draw! ~~")
                    print()
                    break
                else:
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    currentPlayerTurn = switchTurns(currentPlayerTurn)
        elif choice == "i":
            print("#### The 'algorithm' of the game is thus:")
            print("- The user selects a game between one or two players.")
            print("- A one player game has the user play against the computer.")
            print("- A two player game has two users play against one another.")
            print("- Each player takes turns 'dropping' their 'pieces' into the board.")
            print("- The goal is for one player to connect four pieces in an unbroken sequence.")
            print("- A sequence can be horizontal, vertical, or diagonal.")
            print("- The game ends when one player has... FOUR IN SEQUENCE!")
        elif choice == "q":
            running = False
            print("Goodbye!")
        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__":
    main()
