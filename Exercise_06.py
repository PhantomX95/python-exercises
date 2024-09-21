# Write a Python program to get password from user and make sure that
# Password must contain at least one alphabetic character upper and one alphabetic character lower,
# one number, one symbol, and be at most 24 characters long and not less than 6 character.


# Algorithm
# 01: Define a function to validate the password:
#     - Initialize a set containing all valid symbols: !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.
#     - Initialize credentials variables with values False to check if the password contains a symbol, digit, uppercase & lowercase letter.
#     - For loop each character in the password:
#         - If the character is in the symbol set, value "has_symbol" as True.
#         - If the character is a digit, value "has_digit" as True.
#         - If the character is an uppercase letter, value "has_upper" as True.
#         - If the character is a lowercase letter, value "has_lower" as True.
#     - After the loop, check if the password meets all criteria:
#     - Length is between 6 and 24 characters.
#     - Contains at least one uppercase letter, one lowercase letter, one symbol and one digit.
#     - If all conditions are met, return True, otherwise, return False.
# 02: Take input from the user for the password.
# 03: Use the function to validate the password:
#     - If valid, print "Password valid."
#     - If invalid, print an error message explaining the conditions.



def is_password_valid(password):
    """Ensure the password between 6 and 24 characters long,
    contains at least one uppercase letter, one lowercase letter,
    one symbol and one digit or show invalid password"""
    
    # Define symbol set
    symbols = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    # Initialize credential checks
    has_symbol = has_digit = has_upper = has_lower = False
    
    # Check each character in the password
    for char in password:
        if char in symbols:
            has_symbol = True
        elif char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    # Check password length and if it contains at least one upper, one lower, and one symbol and one digit
    if 6 <= len(password) <= 24 and has_upper and has_lower and has_symbol and has_digit:
        return True
    return False

# Take password input from the user
password = input("Enter your password: ")

# Validate the password
if is_password_valid(password):
    print("Password valid")
else:
    print("Password invalid. Ensure it is between 6 and 24 characters long, contains at least one uppercase letter, one lowercase letter, one symbol and one digit.")
