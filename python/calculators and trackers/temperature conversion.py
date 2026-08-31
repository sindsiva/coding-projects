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
# Assignment 3, Problem 3
# Purpose: This program allows the user to choose the conversion type between
# Celsius and Fahrenheit and prompts for the corresponding input to perform the
# required conversion.
# Date Created: October 23, 2025
# Date Modified: November 9, 2025
###################################################################

# This function converts a given Celsius temperature to Fahrenheit.
def celsiusToFahrenheit(celsius):
    return 9 / 5 * celsius + 32 # return value based on formula

# This function converts a given Fahrenheit temperature to Celsius.
def fahrenheitToCelsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32) # return value based on formula

# This function calculates the temperature in a different unit based on the 
# user's choice of temperature conversion and given temperature.
def calculateTemperature():
    choice = input("Enter your choice (1 or 2): ") # ask for user choice
    
    # show error message until user inputs valid choice
    while choice != "1" and choice != "2":
        choice = input("Invalid! Enter your choice (1 or 2): ")
    
    # match choice to temperature measurement name    
    match choice:
        case "1":
            choiceName = "Celsius"
        case "2":
            choiceName = "Fahrenheit"
    
    # ask for input of temperature        
    temperature = input("Enter temperature in " + choiceName + ": ")
    
    # verify that the user's input is a number
    while type(temperature) != float:
        try:
            temperature = float(temperature) # convert input to a float
        except ValueError:
            # give an error message and ask again
            temperature = input("Invalid! Enter temperature in " + choiceName \
                                + ": ")
            
    # match conversion and units to the user's choice
    match choice:
        case "1":
            conversion = celsiusToFahrenheit(temperature)
            oldUnit = "°C"
            newUnit = "°F"
        case "2":
            conversion = fahrenheitToCelsius(temperature)
            oldUnit = "°F"
            newUnit = "°C"
    
    # display results
    print(str(temperature) + oldUnit, "=", str(conversion) + newUnit)

def main():
    print("Temperature Conversion") # display title
    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius") # show options
    calculateTemperature()

# call main function
main()
    