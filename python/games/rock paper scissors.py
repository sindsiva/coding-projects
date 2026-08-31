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
# Assignment 2, Problem 1
# Purpose: This program plays rock-paper-scissors with the user.
# Date Created: September 25, 2025
# Date Modified: September 25, 2025
###################################################################

# import random
import random

# prompt user to choose rock, paper, or scissors
userChoice = int(input("scissor (0), rock (1), paper (2): "))

# generate computer's response
computerChoice = random.randint(0, 2)

# find winner and display result
if userChoice == 0 and computerChoice == 0:
    print("The computer is scissor. You are scissor too. It is a draw")
elif userChoice == 0 and computerChoice == 1:
    print("The computer is rock. You are scissor. The computer wins")
elif userChoice == 0 and computerChoice == 2:
    print("The computer is paper. You are scissor. You win")
elif userChoice == 1 and computerChoice == 0:
    print("The computer is scissor. You are rock. You win")
elif userChoice == 1 and computerChoice == 1:
    print("The computer is rock. You are rock too. It is a draw")
elif userChoice == 1 and computerChoice == 2:
    print("The computer is paper. You are rock. The computer wins")
elif userChoice == 2 and computerChoice == 0:
    print("The computer is scissor. You are paper. The computer wins")
elif userChoice == 2 and computerChoice == 1:
    print("The computer is rock. You are paper. You win")
elif userChoice == 2 and computerChoice == 2:
    print("The computer is paper. You are paper too. It is a draw")
else:
    print("invalid input")