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
# Assignment 3, Problem 4
# Purpose: This program displays employees and their total hours in decreasing
# order of the total hours.
# Date Created: October 24, 2025
# Date Modified: November 9, 2025
###################################################################

# This function gets user input about the number of employees and their hours
# and returns a dictionary of statistics.
def getInput():
    # ask user for number of employees
    employees = input("Enter number of employees: ")
    
    # give error message until user's input is an integer
    while type(employees) != int:
        try:
            employees = int(employees) # convert string input to integer
        except ValueError:
            print("Invalid! Enter an integer.") # display erorr message
            employees = input("Enter number of employees: ") # ask again
    
    statistics = {} # make a dictionary to store employee and their hours
    
    # ask user for daily hours for each employee
    for i in range(employees):
        while True:
            try:
                # ask for daily hours
                hours = input("Enter 7 daily work hours for Employee " + str(i)
                              + " (Mon-Sun): ")
                # split the input into a list of hours
                hours = list(map(int, hours.split()))
                
                if len(hours) != 7:
                    # give an error message if user inputs more than 7 hours
                    print("Invalid! Enter 7 numbers with a space between each.")
                    continue # stay in loop until valid input
                
                if any(hour < 0 or hour > 24 for hour in hours):
                    # give an error message if user inputs hour not between 0-24
                    print("Invalid! Enter hours between 0 and 24.")
                    continue # stay in loop until valid input
                
                break # get out of loop if valid input
            
            except ValueError:
                # give error if input is not integers
                print("Invalid! Enter integers.")

        # store employee and sum of their hours in dictionary
        statistics["Employee " + str(i)] = sum(hours)
    
    # sort from highest to lowest
    sortedStatistics = dict(sorted(statistics.items(), 
                                   key = lambda item: item[1], reverse = True))    
    
    return employees, sortedStatistics # return values

# This function creates a table with the given statistics about the employees.        
def makeTable(statistics):
    print(f'{"Employee":<15s} {"Total Hours":<15s}') # display table headings
    
    employees = list(statistics.keys()) # make list of employees
    
    # print each employee and their hours
    for i in range(len(statistics)):
        employee = employees[i]
        print(f"{employee:<15s} {statistics[employee]:<15}")

def main():
    employees, statistics = getInput() # ask for input and store return values
    if employees > 0: # check that number of employees is greater than 0
        makeTable(statistics) # make table with stored statistics

# call main function
main()