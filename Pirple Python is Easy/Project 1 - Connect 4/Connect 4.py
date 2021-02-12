##################################################
## Project #1: Connect 4
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Importing needed libraries
from termcolor import colored, cprint

# Initializing board state
boardState = [[" ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " "]]

# Assigning colored 'O's for each player
playerOnePiece = colored('O', 'red', attrs=['bold'])
playerTwoPiece = colored('O', 'yellow', attrs=['bold'])


# A function draw board
def drawBoard(p, board):
    # Drawing top boundary of board
    cprint("-" * 15, 'blue')

    # Nested loop for  drawing the board
    for row in range(6):
        for col in range(15):
            if col % 2 == 0:
                cprint("|", 'blue', end="")
            # Drawing board state related to player's moves
            elif col % 2 == 1:

                # Drawing Player 1's move
                if p == 1:
                    cprint(board[row][int(col / 2)], end="")

                # Drawing Player 2's move
                elif p == 2:
                    cprint(board[row][int(col / 2)], end="")

        # Drawing the bottom boundary of the board
        if row != 6:
            cprint("\n" + "-" * 15, 'blue')


# A Function to check if a move is valid
def gameLogic(col):
    # If submitted column is out of range returning false
    if 0 > col or col > 6:
        return False

    # Finding first empty space in the submitted column from bottom to top
    for r in range(5, -1, -1):
        if boardState[r][col] == " ":
            # Recording move of the Player 1's coordinates
            if player == 1:
                boardState[r][col] = playerOnePiece
                # Checking if Player 1 won after that move
                if winCondition(player):
                    drawBoard(player, boardState)
                    print("Player 1 WON !!!")
                    exit()
                return True
            # Recording move of the Player 2's coordinates
            elif player == 2:
                boardState[r][col] = playerTwoPiece
                # Checking if Player 2 won after that move
                if winCondition(player):
                    drawBoard(player, boardState)
                    print("Player 2 WON !!!")
                    exit()
                return True
    # İf none of the conditions aren't matched returning False
    return False


# A function to determine if any of the players won the game
def winCondition(p):
    # For Player 1
    if p == 1:
        # Check horizontal locations for win
        for col in range(4):
            for r in range(6):
                if boardState[r][col] == playerOnePiece and boardState[r][col + 1] == playerOnePiece and \
                        boardState[r][col + 2] == playerOnePiece and boardState[r][col + 3] == playerOnePiece:
                    return True

        # Check vertical locations for win
        for col in range(7):
            for r in range(3):
                if boardState[r][col] == playerOnePiece and boardState[r + 1][col] == playerOnePiece and \
                        boardState[r + 2][col] == playerOnePiece and boardState[r + 3][col] == playerOnePiece:
                    return True

        # Check positively sloped diagonals
        for col in range(4):
            for r in range(3):
                if boardState[r][col] == playerOnePiece and boardState[r + 1][col + 1] == playerOnePiece and \
                        boardState[r + 2][col + 2] == playerOnePiece and boardState[r + 3][col + 3] == playerOnePiece:
                    return True

        # Check negatively sloped diagonals
        for col in range(4):
            for r in range(3, 6):
                if boardState[r][col] == playerOnePiece and boardState[r - 1][col + 1] == playerOnePiece and \
                        boardState[r - 2][col + 2] == playerOnePiece and boardState[r - 3][col + 3] == playerOnePiece:
                    return True
    # For Player 2
    elif p == 2:
        # Check horizontal locations for win
        for col in range(4):
            for r in range(6):
                if boardState[r][col] == playerTwoPiece and boardState[r][col + 1] == playerTwoPiece and \
                        boardState[r][col + 2] == playerTwoPiece and boardState[r][col + 3] == playerTwoPiece:
                    return True
        # Check vertical locations for win
        for col in range(7):
            for r in range(3):
                if boardState[r][col] == playerTwoPiece and boardState[r + 1][col] == playerTwoPiece and \
                        boardState[r + 2][col] == playerTwoPiece and boardState[r + 3][col] == playerTwoPiece:
                    return True
        # Check positively sloped diagonals
        for col in range(4):
            for r in range(3):
                if boardState[r][col] == playerTwoPiece and boardState[r + 1][col + 1] == playerTwoPiece and \
                        boardState[r + 2][col + 2] == playerTwoPiece and boardState[r + 3][col + 3] == playerTwoPiece:
                    return True
        # Check negatively sloped diagonals
        for col in range(4):
            for r in range(3, 6):
                if boardState[r][col] == playerTwoPiece and boardState[r - 1][col + 1] == playerTwoPiece and \
                        boardState[r - 2][col + 2] == playerTwoPiece and boardState[r - 3][col + 3] == playerTwoPiece:
                    return True

    # Determining draw condition
    count = 0
    for r in range(6):
        for col in range(7):
            if boardState[r][col] == " ":
                count += 1
    if count < 1:
        print("I don't know how you guys managed this but it's a draw.")
        exit()


# Initiating the board
player = 1
drawBoard(player, boardState)

while True:
    # Taking a move from Player 1
    if player == 1:
        c = int(input("Player 1's Turn : ")) - 1
        # If it's a valid move drawing it the to board
        if gameLogic(c):
            drawBoard(player, boardState)
            # If Player 1 didn't won with that move giving the turn to Player 2
            player = 2
        # If it isn't a valid move asking for a valid move
        else:
            print("Invalid action! Try again.")

    # Taking a move from Player 1
    elif player == 2:
        c = int(input("Player 2's Turn : ")) - 1
        # If it's a valid move drawing it the to board
        if gameLogic(c):
            drawBoard(player, boardState)
            # If Player 1 didn't won with that move giving the turn to Player 1
            player = 1
        # If it isn't a valid move asking for a valid move
        else:
            print("Invalid action! Try again.")
