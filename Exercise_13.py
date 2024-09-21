# Write a Python program to get an angle from the user,
# find its sine and cosine values in radians, and then convert the results into degrees.


# Algorithm:
# 01: Define function calculate_trig_values(degree)
#       - Import math.
#       - Try for Error handling if user input is not integer.
#       - Convert input degree to radians.
#       - Calculate sin, cos in radians.
#       - Convert sin, cos to degree.
#       - Display sin, cos radians and degree.
# 02: Try for handling input error if not a numeric value:
#       - Loop until the user enter numeric value.
#       - Get user input in variable.
#       - Call the function for user input.

import math

def calculate_trig_values(degree):
    """
    Function to calculate the sine and cosine values of a given angle in degrees,
    convert them to radians, and then convert the results back to degrees,
    MUST import math.
    """
    try:
        # Convert degrees to radians
        radians = math.radians(degree)

        # Calculate sin and cos values in radians
        sin_value = math.sin(radians)
        cos_value = math.cos(radians)

        # Convert sin and cos values back to degrees
        sin_degree = math.degrees(math.asin(sin_value))
        cos_degree = math.degrees(math.acos(cos_value))

        # Display the results
        print(f"The Sine Value In Radians Is: {sin_value}")
        print(f"The Cosine Value In Radians Is: {cos_value}")
        print(f"The Sine Value in Degree Is: {sin_degree}")
        print(f"The Cosine Value In Degree Is: {cos_degree}")
        
    # Handle invalid input (non-numeric values) or other potential errors
    except (ValueError, TypeError) as e:
        print(f"Error! {e}")
while True:
    try:
        # Convert user input into a float
        degree_input = float(input("Please Enter An Angle In Degree: "))
        
        # Call the function to calculate the trig values
        calculate_trig_values(degree_input)

        break # Break the loop if user input in valid

    # Handle cases where the user input is not a valid number
    except ValueError:
        print("Error! Please enter a valid numeric value.")
