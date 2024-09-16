# Write a Python program where the user can generate a range of numbers by specifying the start, end, and step values.


# Algorithm:
# 01: Define function the user specify the start, end and step value.
#       - To specify the start loop until the user input is an integer.
#           - Show the user error if the input is not an integer.
#           - In variable store the start value from user.
#       - To specify the end loop until the user input is an integer.
#           - Show the user error if the input is not an integer.
#           - In varialble store the end value from user.
#       - To specify the steps loop until the user input is an integer.
#           - Show the user error if the input is not an integer.
#           - In variable store the steps value from user.
#       - Loop from the user input assign range (start, end, step) and print the result on the same line.
#           - If the user step >= 0 make the end + 1 for the ascending result.
#           - If the user step < 0 make the end - 1 for descending result.
# 02: Call the function.


def user_generate_numbers ():
    """
    This Function the user can specify the start, end and steps value of the numbers range
    """
    while True: # Keep asking to enter a number if not a number
        try:
            # The user specify the start
            user_start = int(input("Please Enter A Number To Start Generate The Numbers From: "))
            break # Stop the loop if the input is valid

        # Error if the user enter other than integer
        except ValueError:
            print("Error! Please Enter Only Numbers.")

    while True: # Keep asking to enter a number if not a number
        try:
            # The user specify the end
            user_end = int(input("Please Enter A Number To End The Generated Numbers: "))
            break # Stop the loop if the input is valid

        # Error if the user enter other than integer
        except ValueError:
            print("Error! Please Enter Only Numbers.")
            
    while True: # Keep asking to enter a number if not a number
        try:
                # The user specify the step
                user_step = int(input("Please Enter A Number Times to Step In The Generated Numbers: "))
                break # Stop the loop if the input is valid

        except ValueError:
            # Error if the user enter other than integer
            print("Error! Please Enter Only Numbers.")

    
    # Generate the user specified numbers in the same line
    if user_step >= 0:
        for i in range(user_start, user_end + 1, user_step):
            print(i, end=", ")
    elif user_step < 0:
        for i in range(user_start, user_end - 1, user_step):
            print(i, end=", ")


user_generate_numbers()