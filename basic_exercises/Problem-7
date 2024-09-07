# write a program to get 6 numbers to tupel and sum that numbers


# Algorithm:

# 01: Define a function:
#   - Create an empty list numbers to store the input numbers.
#   - Loop for Input Collection:
#       - Make sure user enter a number or else show error
#       - Prompt the user to enter a number (convert it to number).
#       - Append the Number to the list numbers.
#   - Convert List to Tuple:

# 02: After collecting all 6 numbers, convert the numbers list into a tuple called numbers_tuple.
# 03: print the tuple numbers_tuple.
# 04: Print the sum of the numbers.


def get_numbers():
    numbers = []
    for i in range(6):
        while True:  # Loop until a valid number is entered
            try:
                insert_input = int(input(f"Enter Number {i+1}: "))
                numbers.append(insert_input)
                break  # Exit the loop when a valid input is received
            except ValueError as v:
                print(f"Error! Please enter a valid number. {v}")    

    return tuple(numbers)

# Get numbers only once
numbers_tuple = get_numbers()

# Print the tuple and the sum
print(f"The tuple numbers: {numbers_tuple}")
print(f"The sum of the numbers: {sum(numbers_tuple)}")


