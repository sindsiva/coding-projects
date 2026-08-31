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
# Assignment 2, Problem 3
# Purpose: This program generates a random license number with three letters and
# four numbers.
# Date Created: September 25, 2025
# Date Modified: October 2, 2025
###################################################################
# import random
import random

# get three random letters
letter1 = chr(random.randint(ord('A'), ord('Z')))
letter2 = chr(random.randint(ord('A'), ord('Z')))
letter3 = chr(random.randint(ord('A'), ord('Z')))

# get four random numbers
digit1 = str(random.randint(0, 9))
digit2 = str(random.randint(0, 9))
digit3 = str(random.randint(0, 9))
digit4 = str(random.randint(0, 9))

# display result
print("A random vehicle plate number: " + letter1 + letter2 + letter3 + digit1 \
      + digit2 + digit3 + digit4)