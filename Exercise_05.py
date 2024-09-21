# Write a Python program to get marks for student subjects:
# (Mathematics, Science, History, Geography, Chemistry, Physics, English, Biology, Philosophy, Art).
# Calculate the total, average, and percentage of the marks, and display the results to the user.

# Algorithm
# 01: Define function with infinite loop get user mark if is from 0 to 100 and is a number if not print error msg.
# 02: Call the function for each subject and store the result.
# 03: Calculate the total, average and percentage.
# 04: print the results.

def get_mark (subject):
    """create a function that take subject and make sure the mark is in 0 to 100"""
    while True:
        try:
            mark = int(input(f"Please Enter The {subject} Mark: "))
            if not mark in range(0, 101):
                print("Please Enter a mark from 0 to 100")
            else:
                return mark
        except ValueError:
            print("Error! Please Enter Only The Mark")

try:
    # Input the marks for each subject, with validation
    m = get_mark("Mathematics")
    s = get_mark("Science")
    h = get_mark("History")
    g = get_mark("Geography")
    c = get_mark("Chemistry")
    p = get_mark("Physics")
    e = get_mark("English")
    b = get_mark("Biology")
    ph = get_mark("Philosophy")
    a = get_mark("Art")

    # Calculate and store the result in variable
    total = m+s+h+g+c+p+e+b+ph+a
    average = total/10
    percent = int(average)

    print(f"Your Total Marks Are: {total}") # print the total
    print(f"Your Average Mark Is: {average}") # print the average
    print(f"Your Percentage Is: {percent}%") # print the percentage



except Exception as e:
    print(f"Unexpected Error {e}")
