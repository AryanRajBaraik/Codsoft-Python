# Contact Book 

contact_book = {}

# To add a contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contact_book[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"\nContact '{name}' added successfully.\n")

# To view all contacts
def view_contacts():
    if not contact_book:
        print("\nContact book is empty.\n")
    else:
        print("\n--- Contact List ---")
        for name, info in contact_book.items():
            print(f"Name: {name}, Phone: {info['Phone']}")
        print()

# To search contact
def search_contact():
    key = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for name, info in contact_book.items():
        if key in name.lower() or key == info['Phone']:
            print(f"\nContact Found:\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n")
            found = True
            break
    if not found:
        print("\nNo contact found.\n")

# To update contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contact_book:
        print("Leave blank to keep existing value.")
        phone = input(f"New phone (current: {contact_book[name]['Phone']}): ").strip()
        email = input(f"New email (current: {contact_book[name]['Email']}): ").strip()
        address = input(f"New address (current: {contact_book[name]['Address']}): ").strip()
        
        if phone:
            contact_book[name]["Phone"] = phone
        if email:
            contact_book[name]["Email"] = email
        if address:
            contact_book[name]["Address"] = address
        
        print(f"\nContact '{name}' updated successfully.\n")
    else:
        print("\nContact not found.\n")

# To delete contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"\nContact '{name}' deleted successfully.\n")
    else:
        print("\nContact not found.\n")

# User Interface Menu
def menu():
    while True:
        print("==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 to 6.\n")

# Run the menu
menu()
