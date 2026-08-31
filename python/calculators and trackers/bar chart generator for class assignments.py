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
# Assignment 4, Problem 3
# Purpose: This program displays a bar chart window displaying the percentages
# of the overall grade represented by projects, quizzes, the midterm exam, and
# the final exam.
# Date Created: November 9, 2025
# Date Modified: November 12, 2025
###################################################################
from tkinter import * # import tkinter

# This function gets the user's input of the percentages and colors for each 
# task and returns the percentage and color choice.
def getInput(task):
    while True:
        # ask user to enter the percentage
        percentage = input("Enter the percentage for the " + task + ": ")
        try:
            percentage = int(percentage) # change type to integer
            if percentage < 0: # print error if percentage is above 0
                print("Invalid! Enter a percentage above 0.")
                continue
            # ask user to enter color
            color = input("Enter the colour for the " + task + ": ")
            break
        except ValueError: # print error if integer is not inputted
            print("Invalid! Enter an integer")
    
    return percentage, color # return percentage and color

# This function creates a bar chart with tkinter with the given percentages and
# colors from the user.
def makeBarChart(data):
    window = Tk() # create window
    window.title("Bar Chart") # set title
    # create canvas and set dimensions
    canvas = Canvas(window, width = 500, height = 200, bg = "white")
    canvas.pack()
    canvas.create_line(10, 190, 490, 190, tags = "line") # create chart line
    
    try:
        # create bar for Project with given color
        canvas.create_rectangle(18, 190 - data["percentages"][0] * 2, 128, 190, 
                                fill = data["colors"][0], tags = "rect")
        # create text for Project with given percentage
        canvas.create_text(73, 190 - data["percentages"][0] * 2 - 10, 
                           text = "Project -- " + 
                           str(data["percentages"][0]) + "%")
        # create bar for Quizzes with given color
        canvas.create_rectangle(136, 190 - data["percentages"][1] * 2, 246, 190, 
                                fill = data["colors"][1], tags = "rect")
        # create text for Quizzes with given percentage
        canvas.create_text(191, 190 - data["percentages"][1] * 2 - 10, 
                           text = "Quizzes -- " + 
                           str(data["percentages"][1]) + "%")
        # create bar for Midterm with given color
        canvas.create_rectangle(254, 190 - data["percentages"][2] * 2, 364, 190, 
                                fill = data["colors"][2], tags = "rect")
        # create text for Midterm with given percentage
        canvas.create_text(309, 190 - data["percentages"][2] * 2 - 10, 
                           text = "Midterm -- " + 
                           str(data["percentages"][2]) + "%")
        # create bar for Final with given color
        canvas.create_rectangle(372, 190 - data["percentages"][3] * 2, 482, 190, 
                                fill = data["colors"][3], tags = "rect")
        # create text for Percentages with given percentage
        canvas.create_text(427, 190 - data["percentages"][3] * 2 - 10, 
                           text = "Final -- " + 
                           str(data["percentages"][3]) + "%")
        window.mainloop()
        
    except TclError: # print error if color is invalid
        print("Invalid color! Restart.")
    
def main():
    data = {"percentages": [], "colors": []} # set empty data dictionary
    tasks = ["Project", "Quizzes", "Midterm", "Final"] # make tasks list
    while True:
        for i in range(len(tasks)): # ask for input for each task
            percentage, color = getInput(tasks[i]) # store input
            data["percentages"].append(percentage) # add to percentages list
            data["colors"].append(color) # add to colors list
        total = sum(data["percentages"])
        if total != 100: # display error if sum of percentages equal 100
            print("Invalid! Make sure your percentages add to 100.")
            data = {"percentages": [], "colors": []} # reset data dictionary
            continue
        break
    makeBarChart(data) # make bar chart with data
    
main() # call main function
    