# Write a Python program to get two numbers from the user and display the multiplication tables for both numbers.

# Algorithm:
# Ask the user to enter the first number.
# Ask the user to enter the second number.
# Ensure that the user has entered numeric values, display an error message if not.
# Print the number at the top of each multiplication table.
# Create a loop from 1 to 10 to perform the multiplication.
# print the results.

try:
    num_1 = int(input("Enter Your First Number: ")) # the input message for first number
    num_2 = int(input("Enter Your Second Number: ")) # the input message for second number

    print(f"The Multiplcation Table For Number: {num_1}") # the number 1 table
    for i in range(1, 11): # range of the table
        print(i * num_1) # print the table

    print(f"The Multiplcation Table For Number: {num_1}")
    for l in range(1, 11): # range of the table
        print(l * num_2) # print the table

except ValueError: # Error message if user didn't entered a number
    print("Wrong Input! Please Enter a Numeric Value")
    