# Write a python program that generates from 11 to 1 number,
# And their square, cube, and addition of square + cube.


# Algorithm:
# 01: Print the head of the table
# 02: for loop reversed range (11):
#       - Print the number, square, cube, addition (square + cube)

print("The Number:\t\tThe Square:\t\tThe Cube:\t\t(Square + Cube)")

for num in reversed(range(11)):
    print(f"{num}\t\t\t{num ** 2}\t\t\t{num ** 3}\t\t\t{(num ** 2) + (num ** 3)}")
