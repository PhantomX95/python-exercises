# Library Management System (OOP)
# Create a Library class where users can borrow and return books. Maintain a list of books available and books borrowed.
# Add the date of borrow for borrowed books.


from datetime import datetime

class LibrarySystem():
    def __init__(self):
        self.available_books = []   # List to store available books
        self.borrowed_books = {}    # Dictionary to track the borrowed books and the borrowers
        self.library_log = {        # Log for tracking actions in the library
            'added_book': [],
            'borrow_book': [],
            'returned_book': [],
        }
    
    def add_books(self, book):
        self.available_books.append(book)   # Add the book to available books list
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Get current time 
        self.library_log['added_book'].append((book, current_time)) # log the addition of the book
        print(f"'{book}' Has Been Added Successfully.\n")
    
    def borrow_book(self, user, book):
        if book in self.available_books:    # Check if the book is available
            self.available_books.remove(book)   # remove the book from the availables
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Get the current time
            # If there's no users borrowed this book delete it
            if book not in self.borrowed_books:
                self.borrowed_books[book] = []
            self.borrowed_books[book].append((user, current_time))  # Add the book to borrowed books
            self.library_log['borrow_book'].append((user, book, current_time))  # Add the borrow action to the log
            print(f"The User '{user}', Borrowed book '{book}'.\n")
        else:
            print(f"There's No Book With The Name: '{book}'\n")

        
    def return_book(self, user, book):
        if book in self.borrowed_books: # Check if not empty
            for (borrowed_user, _) in self.borrowed_books[book]:    # Find the user want to return
                if borrowed_user == user:
                    # Remove the user from the borrowed list and reassign the other users to the list
                    self.borrowed_books[book] = [(usr, dt) for (usr, dt) in self.borrowed_books[book] if usr != user]
                    # If the book borrowed by only one user and returned it delete the book from the list
                    # (This is if more than one user borrowed two books with the same name)
                    if not self.borrowed_books[book]:
                        del self.borrowed_books[book]
                    self.available_books.append(book)   # Return the book to the availables
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    self.library_log['returned_book'].append((user, book, current_time))    # log the action
                    print(f"The User '{user}' Returned Book '{book}'\n")
                    return
            print(f"The User '{user}', Didn't Borrow This Book '{book}'\n.")
        else:
            print(f"The Book '{book}', Is Not With The Borrowed Books.\n")

    def show_available_books(self):
        if not self.available_books:    # Check if the list is not empty
            print("No Available Books.\n")
        else:
            print("The Available Books:\n")
            for num, book in enumerate(self.available_books, start = 1):
                print(f"{num}. {book}")
            print()

    def show_borrowed_books(self):
        if not self.borrowed_books: # Check if empty
            print("There's No Borrowed Books.\n")
        else:
            print(f"The Borrowed Books:\n")
            for book, users in self.borrowed_books.items():
                for user, date_time in users:
                    print(f"{book} Borrowed by {user}, at {date_time}")
                print()
    
    def show_log(self):
        if all(len(details) == 0 for details in self.library_log.values()):
            print("There's No Actions In Library Log.")

        else:
            print("The Library Log:")
            for action, details in self.library_log.items():
                for info in details:    # Reach the list of tuples
                    if action == 'added_book':
                        if info[0]: # Make sure the user name is not empty before printing
                            print(f"Added a Book '{info[0]}', At {info[1]}")
                
                    elif action == 'borrow_book':
                        if info[0]:
                            print(f"The User '{info[0]}' Borrowed a Book '{info[1]}', At {info[2]}")
                        
                    elif action == 'returned_book':
                        if info[0]:
                            print(f"The User '{info[0]}' Returned a Book '{info[1]}', At {info[2]}")
            print()

def main():
    Library = LibrarySystem()   # Call the function

    while True: # Loop the options
        print("To Add a Book To Library Enter: 1")
        print("To Borrow a Book Enter: 2")
        print("To Return a Book Enter: 3")
        print("To Show The Library Books Enter: 4")
        print("To Show The Borrowed Books Enter: 5")
        print("To Show The Library Log Enter: 6")
        print("To Exit Enter: 7")
        print("-----------------------------------")

        try:    # Handle error if user inpur not an interger
            user_choice = int(input("Please Enter a Number Between 1 and 7: "))
            print("======================================\n")
        except ValueError:
            print("\nInvalid Input! Please Enter a Number Between 1 and 7\n")
            continue

        if user_choice == 1:    # Show the available books then ask for the book name to add
            Library.show_available_books()
            book = input("Enter The Book Name: ")
            Library.add_books(book)
            

        elif user_choice == 2:  # Ask the borrower name and call the borrow method
            user_name = input("Enter The Borrower Name: ")
            Library.show_available_books()  # Show the available books
            borrow_book = input("Enter The Book Name: ")
            Library.borrow_book(user_name, borrow_book)
            
        elif user_choice == 3:  # Ask the borrowers name then call the return method
            user_name = input("Enter The Borrower's Name: ")
            returned_book = input("Enter The Return Book's Name: ")
            Library.return_book(user_name, returned_book)
            
        elif user_choice == 4:
            Library.show_available_books()
            
        elif user_choice == 5:
            Library.show_borrowed_books()

        elif user_choice == 6:
            Library.show_log()

        elif user_choice == 7:
            print("Exiting The Program. Goodbye!")
            break
        else:
            print("\nInvalid Input! Please Enter a Number Between 1 and 7\n")

if __name__ == '__main__':
    main()
    