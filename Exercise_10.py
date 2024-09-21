# write a python program to check a number wether it is even or odd and then find the number square


# Algorithm
# 01: Define function:
#     - Initialize variable for user input and it should be a number only.
#     - Check if the user number (modulus is 0) then even, else it's odd.
#     - Calculate the square of the user number.
#     - Display whether the number is even or odd.
#     - Display the square of the number.
# 02: Call the function.


def even_odd_square():
    """Take number from user and display if even or odd and diplay the square of it"""
    while True:    
        try:
            user_num = int(input("Please Enter A Number: "))
            if user_num % 2 == 0:
                result = "The Number You Entered Is Even."
            else:
                result = "The Number You Entered Is Odd."
            
            result += f"\nThe Square Of The Number You Entered Is {user_num ** 2}"
            return result

        except ValueError:
            print("Error! Please Enter Only Numbers")

# Print the function
print(even_odd_square())
