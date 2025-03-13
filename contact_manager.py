# Contact manager application
contacts = []

def add_contact():
    """Add a new contact ensuring no duplicate names."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    # Check for duplicate names
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact with this name already exists!")
            return

    # Store contact as a tuple
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    """Display all contacts in a formatted manner."""
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nList of Contacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact[0]} - {contact[1]} - {contact[2]}")
    print()

def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip().lower()
    for contact in contacts:
        if contact[0].lower() == name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("Contact not found.")

def update_contact():
    """Update a contact's phone number while keeping other details unchanged."""
    name = input("Enter name to update: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name:
            new_phone = input("Enter new phone number: ").strip()
            contacts[i] = (contact[0], new_phone, contact[2])  # Replace tuple
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    """Delete a contact by name."""
    name = input("Enter name to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name:
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    """Main function to run the menu-driven contact manager."""
    while True:
        print("\nWelcome to Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the application
if _name_ == "_main_":
    main()
  output:
Contact added successfully!
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 2
List of Contacts:
1. Mohana - 8185031447 - mohanakarri0@gmail.com
2. priya - 9000000000 - priya@gmail.com
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1
Enter Name: deepthi
Enter Phone Number: 700043445
Enter Email: deepthi@gmail.com
Contact added successfully!
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: jaggu
Invalid choice. Please try again.
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1
Enter Name: jaggu
Enter Phone Number: 43584855
Enter Email: jaggu@gmail.com
Contact added successfully!
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1
Enter Name: moni
Enter Phone Number: 388596905
Enter Email: moni@gmail.com
Contact added successfully!
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 3
Enter name to search: priya
Contact Found: priya - 9000000000 - priya@gmail.com
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 4
Enter name to update: moni
Enter new phone number: 765908553
Contact updated successfully!
----------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice:
 


