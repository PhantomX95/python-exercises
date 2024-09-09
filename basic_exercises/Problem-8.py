# Write a python Program to get 5 numbers from user in array, Find the maximum number and the minimum number.


# Algorithm:
# 01: Import array module.
# 02: Initialize an empty array (a).
# 03: For each number in loop:
#    - Make sure user enter a number or show error.
#       - Input message for user..
#       - Add the input to the empty array(a).
# 04: Initialize max number variable, index the first element of the array.
# 05: Initialize min number variable, index the first element of the array.
# 06: For each number in loop:
#    - Check if the number is greater than max number variable.
#       - Update max number variable.
# 07: For each number in loop:
#    - Check if the number is less than min number variable.
#       - Update min number variable.
# 08: after the loop over the variable max number contain the maximum number and the variable min number contain the minimum number.
# 09: print the max number and the min number.


# Import array module.
import array as arr

# Initialize an empty array
a = arr.array("i", [])

# user insert 5 numbers
for i in range(5):
    while True:
        try:
            num = int(input(f"Enter the number {i + 1}: ")) # the user input as integer
            a.append(num) # add the input to the array
            break # break after input
        except ValueError: # Error, if the user didn't enter integer
            print("Wrong input! Please Enter Only Numbers.")

max_number = a[0]
min_number = a[0]

for number in a:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number


print(f"The Maximum Number Is {max_number}: ")
print(f"The Minimum Number Is {min_number}: ")
