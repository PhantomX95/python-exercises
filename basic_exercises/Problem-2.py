    # Write A Python Program To Take Mark From The User To Check Whether User Able To Admission In College Or Not.
    # If the Marks Is Less Than 60 Then It Don’t Allow To Take Admission.
    # Expected Result if the user input 50 then: Sorry! Your mark does not allow you to join our college. You needed 10 more points to be accepted.

# Algorithm:
# 01: Ask the user to insert his mark
# 02: Use if statement to print if the user is able to addmission in collage or not

mark = int(input("Please Enter Your Mark: ")) # Take the user mark

if mark < 60 : # Check if user is accepted or not and print message.
    print(f"Sorry! Your mark does not allow you to join our college, You needed {60 - mark} more points to be accepted")
else:
    print("Congrats, Your mark allows you to join our college")