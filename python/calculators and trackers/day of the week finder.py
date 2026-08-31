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
# Assignment 2, Problem 4
# Purpose: This program calculates the day of the week based on Zeller's
# congruence and the given year, month, and day of the month.
# Date Created: September 25, 2025
# Date Modified: October 2, 2025
###################################################################

# prompt user for year, month, and day
year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day = int(input("Enter the day of the month: 1-31: "))

# calculate day of the week
if month == 1:
    month = 13
    year -= 1
if month == 2:
    month = 14
    year -= 1
dayOfWeek = (day + (26 * month + 26) // 10 + year % 100 + year % 100 // 4 +\
    year // 100 // 4 + 5 * (year // 100)) % 7

# identify day of the week
match dayOfWeek:
    case 0: dayName = "Saturday"
    case 1: dayName = "Sunday"
    case 2: dayName = "Monday"
    case 3: dayName = "Tuesday"
    case 4: dayName = "Wednesday"
    case 5: dayName = "Thursday"
    case 6: dayName = "Friday"

# display result
print("Day of the week is", dayName)
