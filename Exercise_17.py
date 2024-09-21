# Write a Python program to find the occurrence of a specific word or character in a text. Then,
# ask the user if they want to replace it and perform the replacement if they say yes.


# Algorithm:
# 01: Define function:
#       - Ask user to enter a sentence, store it in variable.
#       - Ask the user y to replace it or n for exit and store the answer in variable.
#           - If user entered y show message choose the sentence or char you want to replace, store it in variable.
#               - Show how many times it repeated.
#               - Display message enter the text replacement, store it in variable.
#               - Replace the text
#               - Display the new message
#           - If user entered n show the entered text.
#           - Else show error message please enter y/n.
# 02: Call the function to excute

def find_replace():
    """
    Find and replace specific word, character or sentence from user text, and replace it depend on user choice
    """
    # Prompt the user to enter a text
    user_text = input("Please enter your text here: ").strip()

    # Ask the user if they want to replace anything
    user_choice = input("Do you want to replace any word, character, or sentence? Enter Y/N: ").strip().lower()
    
    # If the user wants to make a replacement
    if user_choice == 'y':
        
        # the text user wants to replace
        search_term = input("Enter the sentence, word, or character you want to replace: ")
        
        # Count how many times the search term appears in the text
        repeated = user_text.count(search_term)

        # If the search term is found in the text
        if repeated > 0:

            # Print the number of times the search term repeated
            print(f"'{search_term}' is repeated {repeated} {'time' if repeated == 1 else 'times'}")
            
            # Get the user replacement text
            replacement = input("Enter your replacement text: ")
            
            # Replace the search term with the replacement text
            new_text = user_text.replace(search_term, replacement)
            
            print("Text updated.")
            print(f"Your new text is:\n{new_text}") # Print the new message

        # If search term doesn't exist in the text
        else:
            print(f"'{search_term}' doesn't exist in your text.")
    
    # If user doesn't want to replace anything
    elif user_choice == 'n':
        
        # Print the original text
        print(f"Your text is:\n{user_text}")
    
    # If the user input an invalid choice
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

# Call the function
find_replace()

