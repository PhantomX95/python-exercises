# Write a Python program to prompt the user for a number, validate the input,
# and then display all numbers between 1 and 100 that can divide the entered number without leaving a remainder.




# Algorithm:
# 01: Define function show all numbers between 1 and 100 that can divide the entered number without leaving a remainder:
#       - Handle invalid inputs (non-integer entries) by displaying an error message and prompting again until a valid number is entered.
#       - Store the user-entered number in a variable.
#       - Initialize an empty list to keep track of numbers that divide the user-entered number.
#       - loop Range (1, 101) and if the user number modulus = 0 store in new variable divisible_numbers.
#       - Display the results
# 02: Call the function


def can_divided_by():
    """function show all numbers between 1 and 100 that can divide the entered number without leaving a remainder"""
    while True:
        try:
             # Prompt the user to enter a number
            user_num = int(input("Please Enter A Number: "))

            break # Exit the loop if the input is valid

        except ValueError:
            # Handle invalid input
            print("Error! Please Enter Only A number.")
    
    divided_by_nums = []

    # Check if the user_num is divisible by "i" and insert it in divided_by_nums list 
    for i in range(1,101):
        if user_num % i == 0:
            divided_by_nums.append(i)
    
    # Display the results
    if divided_by_nums:
        print(f"The numbers from 1 to 100 that are divisible by {user_num} are:")
        print(divided_by_nums)
    else:
        print(f"There are no numbers between 1 and 100 divisible by {user_num}.")

can_divided_by()