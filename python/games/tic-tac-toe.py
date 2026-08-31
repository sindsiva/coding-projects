###################################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Student Name: Sindhu Sivasankar
# Student Number: 1009813686
# Supervisor: Dr. Maher Elshakankiri
#
#
# Assignment 4, Problem 1
# Purpose: This program simulates a tic-tac-toe game with two players.
# Date Created: November 8, 2025
# Date Modified: November 12, 2025
###################################################################

# create global dictionary of tic-tac-toe grid
rows = {0: ["  |", "  |", "  |"], 1: ["  |", "  |", "  |"], 
        2: ["  |", "  |", "  |"]}

# This function displays the tic-tac-toe grid, including the border and global
# dictionary of rows and columns.
def makeGrid():
    border = "-------------" # create border   
    print(border) # print border
    print("| " + " ".join(rows[0])) # print row 0
    print(border) # print border
    print("| " + " ".join(rows[1])) # print row 1
    print(border) # print border
    print("| " + " ".join(rows[2])) # print row 2
    print(border) # print border

# This function allows the given player to choose a row and column on the grid,
# printing an error message if the choice is not available.
def getInput(player):
    while True:
        try:
            # ask for row
            row = input("Enter a row for " + player + ": ")
            row = int(row) # change type to integer
            if row not in range(0, 3): # check if row is within grid
                print("Invalid! Row not in grid.") # print error if not
                continue
            # ask for column
            column = input("Enter a column for " + player + ": ")
            column = int(column) # change type to integer
            if column not in range(0, 3): # check if column is within grid
                print("Invalid! Column not in grid.") # print error if not
                continue
            if rows[row][column] != "  |": # check if row/column is free
                # print error if occupied
                print("Invalid! Position already occupied.")
                continue
            break
        except ValueError: # check if input can be an integer
            print("Invalid! Not valid integer.") # print error if not
    
    return row, column # return row and column of user's choice

# This function updates the tic-tac-toe grid based on the player and their
# chosen row and column.
def updateGrid(player, row, column):
    if player == "player X": # check which player is playing
        rows[row][column] = "X |" # print X in chosen position for Player X
    else:
        rows[row][column] = "O |" # print O in chosen position for Player O

# This function checks if a player has won based on whether they have placed
# three of their symbols in the same row, column, or diagnol.
def findWinner():
    winner = "" # keep winner empty to check later
    for row in rows: # check if either player has three symbols in same row
        if rows[row] == ["X |", "X |", "X |"]:
            winner = "Player X"
        if rows[row] == ["O |", "O |", "O |"]:
            winner = "Player O"
    # check if either player has three symbols in same column
    for i in range(len(rows[1])): 
        if rows[0][i] == rows[1][i] == rows[2][i] == "X |":
            winner = "Player X"
        if rows[0][i] == rows[1][i] == rows[2][i] == "O |":
            winner = "Player O"
    # check if either player has three symbols in same diagnol
    if rows[0][0] == rows[1][1] == rows[2][2] == "X |":
        winner = "Player X"
    if rows[0][0] == rows[1][1] == rows[2][2] == "O |":
        winner = "Player O"
    if rows[0][2] == rows[1][1] == rows[2][0] == "X |":
        winner = "Player X"
    if rows[0][2] == rows[1][1] == rows[2][0] == "O |":
        winner = "Player O"

    return winner # return winner

def main():
    makeGrid() # display the starting grid
    for i in range(1, len(rows[0]) ** 2 + 1): # play until grid fills up
        if i % 2 != 0: # alternate player turns
            player = "player X"
        else:
            player = "player O"
        row, column = getInput(player) # store player's choice of row/column
        updateGrid(player, row, column) # update the grid based on choice
        winner = findWinner() # check if there is a winner
        makeGrid() # display the updated grid
        if winner != "": 
            print(winner, "won") # print the winner if a player won
            break # close the loop if a player won
        elif i == len(rows[0]) ** 2:
            print("Draw") # print draw if grid fills up but no winner       

main() # call main function