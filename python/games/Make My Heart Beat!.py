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
# Midterm Project
# Purpose: The program allows the user to choose a cheesey pick-up line and 
# creates a random graphic of a heartbeat with the computer's reaction.
# Date Created: October 8, 2025
# Date Modified: October 15, 2025
###################################################################

# import libraries
from random import randint
import turtle

# declare constants
FACTOR = randint(4, 10) # use to create random heartbeat line and reaction

# This function displays the pick-up line options, asks the user for input, and
# verifies the input.
def getPickUpLine():
    # display pick-up line options
    print("Welcome to Make My Heart Beat! Choose your pick-up line to start:")
    print("")
    print("1. Are you a camera? Because all I do is smile at you.")
    print("2. I think I lost my phone number. Can I have yours?")
    print("3. Are you tired? 'Cause you’ve been running through my mind.")
    print("4. I’m lost. Can you give me directions to your heart?")
    print("5. Is there an airport nearby or is it my heart taking off?")
    print("6. Do you believe in love at first sight or should I pass by again?")
    print("7. If nothing lasts forever, will you be my nothing?")
    print("8. I must be in a museum, because you truly are a work of art.")
    print("9. Are you a dictionary? 'Cause you’re adding meaning to my life.")
    print("10. We’re not socks, but I think we’d make a great pair.")
    print("")
    
    # ask user for input
    line = input("Enter the number of the line you want to say: ")
    
    # verify input
    while line not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        line = input("Invalid!\nEnter the number of the line you want to say: ")

# This function sets the turtle screen and draws a random heartbeat line based
# on a random factor.
def drawHeartbeatLine():
    # set up screen
    screen = turtle.Screen()
    screen.setup(width = 800, height = 600)
    
    # set up starting position and distance between beats
    x = -375
    y = 0
    beatSpace = 200 - (FACTOR * 20)
        
    # set up turtle settings
    turtle.speed(FACTOR - 3)
    turtle.pensize(3)
    turtle.color("red")
    
    # draw the heartbeat line
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for i in range(1, FACTOR):
        turtle.goto(x, y)
        turtle.forward(beatSpace) # starting line
        x += beatSpace # update x
        turtle.goto(x + 10, y + 30) # first peak
        x += 10 # update x
        turtle.goto(x + 10, y - 10) # back down
        x += 10 # update x
        turtle.forward(5) # move forward
        x += 5 # update x
        turtle.goto(x + 10, y + 100) # second peak
        x += 10 # update x
        turtle.goto(x + 10, y - 30) # back down
        x += 10 # update x
        turtle.forward(5) # move forward
        x += 5 # update x
        turtle.goto(x + 10, y) # third peak
        x += 10 # update x
    
    # draw the ending line
    turtle.forward(beatSpace)
    turtle.penup()
    turtle.hideturtle()

# This function displays the computer's reaction based on the heartbeat line.
def displayReaction():
    turtle.speed(10)
    turtle.color("black")
    turtle.goto(-375, -150)
    turtle.pendown()
    if FACTOR in range(4, 6):
        turtle.write("Ew, what? We're just friends.", font = ("Georgia", 24))
    elif FACTOR in range(6, 8):
        turtle.write("Haha. I guess that's sweet.", font = ("Georgia", 24))
    else:
        turtle.write("Oh wow...you're making me blush.", font = ("Georgia", 24))
    turtle.penup()
    turtle.hideturtle()
    turtle.done()
    
def main():
    getPickUpLine()
    drawHeartbeatLine()
    displayReaction()
    
# call main function
main()