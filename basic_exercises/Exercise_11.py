# Write a python program to get 5 years in array and display only the leap years

# Algorithm:
# 01: Function check if the year is leap:
#       -It is divisible by 4, but not by 100 unless also divisible by 400.# 01: Import array.
# 02: Import array
# 03: Function:
#       - Initialize an empty integer array.
#       - Use a loop to prompt the user for 5 year inputs:
#           - If the input is not a valid integer, display an error message.
#           - If the input is valid, append it to the array.
#           - stop the loop
#       - Initialize variable leap_years array and loop the array previous array and call the function to find the leap ones.
#       - if the leap_years array is not empty display the result
#           - or show there's no leap year entered.
# 04: Call the Function that shows the result


def leap_year(year):
    """Check if a given year is a leap year."""

    # A leap year is divisible by 4 and not divisible by 100, unless divisible by 400
    return (year % 4 == 0 and year % 100 != 0 and year != 0) or (year % 400 == 0 and year != 0)

import array as arr

def show_leap_year():
    """Get 5 years from user and display the leap years"""

    # Initialize an empty array to store the years
    years = arr.array("i", [])

    # Loop to get 5 year inputs from the user    
    for i in range(5):
        while True: # Keep asking until valid input is entered
            try:
                # Ask the user to input a year
                year = int(input(f"Enter The Year {i + 1}: "))
                years.append(year)
                break # Exit loop when valid input is given

            # If the user inputs anything that is not a valid integer, show an error
            except ValueError:
                print("Error! Please Enter a Valid Year.")

    # Initialize another array to store only the leap years
    leap_years = arr.array("i", [year for year in years if leap_year(year)])

    # If there are leap years in the array, display them
    if len(leap_years) > 0:
        for year in leap_years:
            print(f"The Year {year}, Is a Leap Year")
    else:
        print("There Are No Leap Years In Your Entries.")

# Call the function to show leap years
show_leap_year()