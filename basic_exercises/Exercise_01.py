# Write a Python program to show such type of layout of numbers, square and cube to numbers 1to5:

# Algorithm:
# 01: Print the header row with columns "Number", "Square", and "Cube".
# 02: Generate numbers from 1 to 5 using a loop.
# 03: Calcuate: Square of the number (square = number * number) Cube of the number (cube = number * number * number)
# 04: Print: The number, its square, and its cube, each formatted to align in columns.

# Print the header
print(f"{'Number'}\t\t{'Square'}\t\t{'Cube'}")

for num in range(1, 6): # Generate Numbers 1 to 5 in loop
    square = num ** 2 # square = number * number
    cube = num ** 3 # cube = number * number * number
    print(f"{num}\t\t{square}\t\t{cube}")
