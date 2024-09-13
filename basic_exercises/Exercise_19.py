# Write a Python program that asks the user to enter fullname, a valid URL, a valid gmail,
# and a password that includes at least one special character, one uppercase letter, one lowercase letter, and one number.



# Algorithm:
# 01: Import re module.
# 02: Valid function take fullname parameter:
#       - Regular expression the fullname only take firstname space lastname.
#       - If regex fullname print valid else invalid.
# 03: Valid function take URL parameter:
#       - Regular expression the URL.
#       - If regex URL print valid else invalid.
# 04: Valid function take gmail parameter:
#       - Regular expression the gmail only take only numbers, alpha or ._-.
#       - If regex gmail print valid else invalid.
# 05: Valid function take password parameter:
#       - Regular expression the password must contain at least one special character, one uppercase and one lowercase letter and one number.
#       - If regex password print valid else invalid.
# 06: Ask user to enter URL.
#       - Call function URL.
#           - If true print valid URL if not show error message.
# 07: Ask user to enter gmail.
#       - Call function gmail.
#           - If true print valid gmail if not show error message.
# 08: Ask user to enter password.
#       - Call function password
#           - If true print valid password if not show error message.

import re

def full_name_valid(name):
    """Regex to match a name with first and last name, each 2-16 characters long"""
    # Regex pattern to validate full name
    name_regex = r"^[A-Za-z]{2,16}\s[A-Za-z]{2,16}$"
    if re.match(name_regex, name):
        return True
    return False

def link_valid(URL):
    URL_regex = r"^(https?://)?(www.)?([A-Za-z0-9-]{1,32}\.)+[A-Za-z]{2,6}$"
    if re.match(URL_regex, URL):
        return True
    return False

def gmail_valid(email):
    email_regex = r"^[A-Za-z0-9._-]{2,32}@gmail.com$"
    if re.match(email_regex, email):
        return True
    return False

def password_valid(password):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[\w\d@$!%*?&^]{4,24}$"
    if re.match(password_regex, password):
        return True
    return False

try:
    while True:
        full_name = input("Please Enter Your Full Name: ")
        if full_name_valid(full_name):
            print("Name is valid")
            break
        else:
            print("Invalid Name Format. Please Enter a First Name And Last Name, Each 2-16 Characters Long.")
except Exception :
    print(f"An error occurred.")


try:
    while True:
        url = input("Please Enter Your URL: ")
        if link_valid(url):
            print("URL is valid")
            break
        else:
            print("Invalid URL Format Please Enter: https://www.domain.com https://domain.com or domain.com.")
except Exception :
    print(f"An error occurred.")


try:
    while True:
        gmail = input("Please Enter Your Gmail: ")
        if gmail_valid(gmail):
            print("Gmail is valid")
            break
        else:
            print("Invalid gmail format, Please Enter a Valid Gmail")
except Exception :
    print(f"An error occurred.")


try:
    while True:
        password = input("Please Enter a Password Must Contain At Least One Special Character, One Uppercase Letter, One Lowercase Letter, And One Number: ")
        if password_valid(password):
            print("Password is valid")
            break
        else:
            print("Invalid Password format. The Password Must Contain At Least One Special Character, One Uppercase Letter, One Lowercase Letter, And One Number.")
except Exception :
    print(f"An error occurred.")
