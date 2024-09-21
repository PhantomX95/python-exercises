# create a simple contact book program that allows you to add, update, and delete contacts.
# Each contact will have a name and phone number. You should be able to perform the following actions:
# Add a Contact: Add a new contact to the contact book.
# Update a Contact: Update an existing contact’s phone number.
# Delete a Contact: Remove a contact from the contact book.
# List All Contacts: Print out all contacts in the contact book.
# Find a Contact: Look up a contact by name and display their phone number.




# Algorithm:
# 01: Create a class ContactBook that includes:
#       - An attribute contacts to store contacts as a dictionary.
#       - Methods for adding, updating, deleting, listing, and finding contacts.
# 02: Define function to check phone number validity: return true if the number isdigit and 11 long
# 03: Define methods in the ContactBook class:
#       - add_contact(name, phone_number):
#               - If name is already in contacts, print an error message else add name and phone_number to contacts.
#       - update_contact(name, new_phone_number):
#               - If name is in contacts, update its phone number else print an error message.
#       - delete_contact(name):
#               - If name is in contacts, remove it from contacts else print an error message.
#       - list_all_contacts():
#               - If contacts is empty, print a message indicating no contacts are available else print each contact's name and phone number.
#       - find_contact(name):
#               - If name is in contacts, print its phone number else print an error message.
# 04: Create the Main Function:
#       - Initialize the Contact Book Object an instance of the ContactBook class.
#       - Display the Menu with options to add, update, delete, list, find contacts, or exit.
#       - Use a while loop to continually display the menu and process user choices.
#       - For each choice:
#               - 'Add' prompt for name and phone_number then call add_contact(name, phone_number).
#               - 'Update' prompt for name and new_phone_number then call update_contact(name, new_phone_number).
#               - 'Delete' prompt for name call delete_contact(name).
#               - 'List contact' call list_all_contacts().
#               - 'Find Contact' prompt for name and call find_contact(name).
#               - 'Exit' display an exit message and break the loop.
#       - Raise a ValueError for choices not between 1 and 6.


class Contact_Book:
    def __init__(self):
        # Dictionary to store contact names and phone numbers
        self.contacts = {}
    
    def Phone_Valid(self, Phone_Number):

        # Check if the phone number is exactly 11 digits long and contains only digits
        return len(Phone_Number) == 11 and Phone_Number.isdigit()
    
    def add_contacts(self, Name, Phone_Number):

        # Validate phone number
        if not self.Phone_Valid(Phone_Number):
            raise ValueError("Wrong Input! Please Enter A Valid Phone Number Contain 11 Numbers.")
        
        # If the name already exists in contacts
        if Name in self.contacts:
            while True:

                # Ask user if they want to update the existing contact
                user_choice = input(f"The Name {Name}, Already Exist In The Contact Book, Do You Want To Update It Y/N: ").lower()
                if user_choice == 'y':
                    self.update_contact(Name)  # Update contact details
                    break
                elif user_choice == 'n':
                    print("Contact Not Updated.")
                    break
                else:
                    print("Wrong Input! Please Enter Y/N.")

            return  # Exit if the name exists

        # If the phone number already exists in contacts
        elif Phone_Number in self.contacts.values():

            # Find the name associated with the existing phone number
            contact_name = next(name for name, number in self.contacts.items() if number == Phone_Number)
            print(f"The Number '{Phone_Number}', Already Exist In The Contact Book Assigned To '{contact_name}'.")
        
        else:
            # Add the new contact
            self.contacts[Name] = Phone_Number
            print(f"The Contact '{Name}', Added With Phone Number: '{Phone_Number}'.")
    
    def update_contact(self, Name):

        # Check if the contact exists
        if Name not in self.contacts:
            print(f"The Contact '{Name}', Doesn't Exist In The Contact Book.")
            return
        
        # Ask for new contact name
        new_name = input("Enter the new contact name (Leave Blank To Keep The Current Name): ")
        if new_name in self.contacts and new_name != Name:
            print(f"The Name '{Name}', Already Exists In Contact Book.")
            return
        
        # Ask for new phone number
        new_phone = input("Enter New Phone Number: ")
        if not self.Phone_Valid(new_phone):
            print("Wrong Input! Please Enter A Valid Phone Number Contain 11 Numbers.")
            return
        
        # Check if the new phone number already exists
        if new_phone in self.contacts.values():
            while True:

                # Ask user if they want to see which contact has the same phone number
                user_choice = input(f"The Number:{new_phone}, Is Already Assigned To Another Contact, Do You Want To Show The Contact Enter Y/N: ").lower()
                if user_choice == 'y':
                    for key, value in self.contacts.items():
                        if value == new_phone:
                            print(f"Name: {key}.\nPhone Number: {value}.")
                            break
                    break
                elif user_choice == 'n':
                    break
                else:
                    print("Wrong Input! Please Enter Y/N: ")
        else:
            # Update or add the contact with new details
            self.contacts[new_name or Name] = new_phone
            print("Successfully Added.")

    def delete_contact(self, Name):

        # Delete the contact if it exists
        if Name in self.contacts:
            del self.contacts[Name]
            print(f"Contact '{Name}' Deleted Successfully.")
        else:
            print(f"Contact '{Name}' Doesn't Exist.")

    def list_contacts(self):

        # List all contacts
        if not self.contacts:
            print("No Contact In The Contact Book.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def find_contact(self, Name):
        
        # Find and display contact details
        if Name in self.contacts:
            print(f"{Name}: {self.contacts[Name]}")
        else:
            print(f"There's No Contact With Name: '{Name}'.")

def main():
    contact_book = Contact_Book()
    while True:
        print("=" * 30)
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Find Contact")
        print("6. Exit")
        print("=" * 30)

        try:
            user_choice = int(input("Enter Your Choice (1-6): "))

            if user_choice == 1:
                Name = input("Please Enter The Contact Name: ")
                Phone = input("Please Enter The Phone Number: ")
                contact_book.add_contacts(Name, Phone)
            
            elif user_choice == 2:
                Name = input("Please Enter The Contact Name To Update: ")
                contact_book.update_contact(Name)

            elif user_choice == 3:
                Name = input("Please Enter The Contact Name To Delete: ")
                contact_book.delete_contact(Name)

            elif user_choice == 4:
                print("Contact List:")
                contact_book.list_contacts()
            
            elif user_choice == 5:
                Name = input("Please Enter The Contact Name To Find: ")
                contact_book.find_contact(Name)
            
            elif user_choice == 6:
                print("Exiting The Contact Book.")
                break

            else:
                raise ValueError("Wrong Input! Please Enter A Number Between 1 and 6.")

        except ValueError:
            print("Wrong Input! Please Enter A Number")

if __name__ == "__main__":
    main()

    