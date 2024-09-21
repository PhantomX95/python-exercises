# Write a Python program to check if the user-inputted number is prime or not.



# Algorithm:
# 01: Define a function to find the prime number:
#       - The number must be > 1
#       - For loop the number Check divisibility range from 2 up to the square root,
#           if it can be divided by a number greater than its square root,
#           it must also be divisible by a number smaller than the square root
#       - If % == 0 it's not prime if not it's prime.
# 02: Error handling if user inpt is not integer.
# 03: Store the user number in variable.
# 04: If function the num display message the number is prime else display not a prime number.


def is_prime(num):
    """
    This function is to find the prime number
    """
    # Prime number must be > 1
    if num <= 0:
        return False
    
    for i in (2, (num ** 0.5) + 1): # Check divisibility up to the square root
        if num % i == 0:
            return False # If divisible, it's not prime
    
    return True # If no divisors are found, it's prime

# Check the user input if it's prime number
try:
    # User input number
    user_num = int(input("Enter A Number To Check If It's Prime Or Not: "))
    if is_prime(user_num):
        # Show the prime number message
        print(f"The Number {user_num} Is A Prime Number.")
    
    else:
        # Show not a Prime number message
        print(f"The Number {user_num} Is Not A Prime Number.")

    
except ValueError: # Error if input is not integer
    print("Error! Please Enter Only Numbers.")
