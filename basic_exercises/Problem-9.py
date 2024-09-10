# Write a Python program to get two numbers and an operator from the user to perform an arithmetic operation.
# If the user inputs an invalid operator, restrict the operation and display an error message to the user.

# Algorithm
# 01: Input the first number, error if the user enter other than numbers.
# 02: Input the second number, error if the user enter other than numbers.
# 03: Input Operator: (+, -, *, /), error if not in the valid ones.
# 04: perform operator:
#   - if "+" add the two numbers.
#   - if "-" subtract the second number from the first.
#   - if "*" multiply the two numbers.
#   - if "/":
#       - if second number is 0, show error message.
#       - othrerwise divide the first number from the second.
# 05: Print the two numbers with the result


def perform_operation ():
    while True:
        try:

            # Get valid input for the first number
            while True:
                try:
                    num1 = int(input("Enter The First Number: "))
                    break # Exit the loop if input is valid
                except ValueError:
                    print("Error! Please Enter Only Numbers.")

            # Get valid input for the second number
            while True:
                try:
                    num2 = int(input("Enter The Second Number: "))
                    break # Exit the loop if input is valid
                except ValueError:
                    print("Error! Please Enter Only Numbers.")

            # Get valid input for the operator
            while True:
                    operator = input("Enter an operator(+, -, *, /): ")
                    if operator in ['+', '-', '*','/' ]:
                        break # Exit the loop if input is a valid operator
                    else:
                        print("Error! Invalid Operator.")

            # Perform the calculation based on the operator
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "Error! Division By Zero Is Not Allowed."
                result = num1 / num2

            # Return the result if everything is valid
            return f"The Result Of {num1} {operator} {num2} = {result}"
        
        # If the user enters a non-number where a number is expected, catch the error
        except ValueError:
            print("Error! Please Enter Only Numbers")


# Call the function and print the result
print(perform_operation())



