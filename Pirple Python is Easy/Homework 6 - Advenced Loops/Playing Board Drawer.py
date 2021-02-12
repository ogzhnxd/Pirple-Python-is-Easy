##################################################
## Homework Assignment #3: "If" Statements
## Playing Board Drawer
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Quick Note : I'm using PyCharm IDE for this homework and when i maximize built in Terminal that is in the IDE i can fit 20 by 111 board in it.

# Function to check if parameters is in range
def doesItFit(rows, columns):
    # Returning to if parameters is in the range
    if 2 < rows < 21 and 2 < columns < 112:
        return True

    # Printing an error message and returning False if parameters isn't in the range
    else:
        print("Board dimensions is not in range!")
        print("For rows you should enter a number between 2-20 (including 2 and 20)")
        print("For columns you should enter a number between 2-111 (including 2 and 112)")
        return False


# Function to draw boards
def boardDrawer(rows, columns):
    # Returning False if board doesn't fit with given parameters
    if not doesItFit(rows, columns):
        return False

    # Logic formulas for printing board (Note : i found these formulas by trial and error :D)
    horizontalLineFormula = (2 * columns) - 1
    rowLogicFormula = (2 * columns - 2) + 1

    # Two Nested for loops for drawing the board
    for x in range(rows):

        for y in range(0, rowLogicFormula):

            # Printing " " in current x row if y index is divisible with "2"
            if y % 2 == 0:
                print(" ", end="")
            # # Printing "|" in current x row if y index's remainder is "1" when divided by "2"
            elif y % 2 == 1:
                print("|", end="")

        # Switching the next line
        print("")
        # Printing the right amount of "-" character for given dimensions
        if x != rows - 1:
            print(horizontalLineFormula * "-")

    return True


# Printing the board and result
print(boardDrawer(20, 20))
