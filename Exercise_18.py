# Write a Python program to get the names of ten students, display them on the screen,
# and allow the user to update any student's name at runtime.


# Algorithm:
# 01: Define a function:
#       - Initialize an empty list.
#       - Loop for user to enter student name 10 times numeric and append in the empty list.
#       - Display and enumerate the student names
#       - Loop ask if the user want to update any student name Y/N.
#           - If user entered Y.
#               - Prompt user to enter a number from 1, 10.
#                   - If user enter in range 1, 10.
#                        - Prompt user to enter the new student name.
#                        - Find the student name index and update it.
#                        - Show message student name updated successfully.
#                        - Loop print the students name with numeric value.
#                   - If user enter number not in range 1, 10 or str show error message.
#           - If user entered N break the loop.
#           - If user Other than Y/N show error message.
# 02: Call the function to excute.


def student_name_update():
    """
    This function to enter 10 student name and update them
    """
    
    student_list = []
    # Keep ask to enter until the 10 names entered
    while True:
        # Ask user to enter the student name 10 times and append in the list
        for i in range(1, 11):
                student_name = str(input(f"Enter The Student Name Number {i}:"))
                student_list.append(student_name)
        break # Break after all 10 names are entered
    
    # Display list of the student names
    print("The Student Names:")
    for i, name in enumerate(student_list, 1):
         print(f"{i}. {name}")
    
    while True: # Keep asking until valid input
        user_choice = input("Do You Want To Update A student's Name? Enter Y/N: ").strip().lower()


        if user_choice =='y':
            while True:
                try: # To handle error if unput is not a numeric value
                        
                    # Prompt user to enter the student's number want to update
                    student_number_update = int(input("Please Enter The Student Number (1, 10) You Want To Update: "))
                    
                    # Continue updating if user enter 1, 10
                    if 1 <= student_number_update <= 10:

                        # Take the new student's name from user and update the name 
                        new_student_name = input("Please Enter The New Name: ")
                        student_list[student_number_update - 1] = new_student_name
                        
                        # Show success message and display the new list
                        print("The Student Name Updated.")
                        print(f"The New Student's Names List: ")
                        
                        for i, name in enumerate(student_list, 1):
                         print(f"{i}. {name}")

                        break # Stop loop after successfully update the name
                    # If user enter a number other than 1 to 10
                    else:
                        print("Error Please Enter a Number From 1 to 10")
                    # Error if user enter a string
                except ValueError:
                    print("Invalid Input! Please Enter a Valid Number (1, 10).")
                 
        # If user enter 'n' stop program
        elif user_choice == 'n':
            break
        
        # Show error if the input is not 'Y' or 'N'
        else:
            print("Wrong Input! Please Ente Y/N Only.")


student_name_update()