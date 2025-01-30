class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update_contact(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\nAdd a new contact:")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
            return
        print("\nList of Contacts:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self):
        search_term = input("\nEnter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
                found = True
        if not found:
            print("No contact found with that name or phone number.")

    def update_contact(self):
        name = input("\nEnter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found. You can update the details.")
                new_name = input(f"Enter new name (or press Enter to keep {contact.name}): ") or contact.name
                new_phone = input(f"Enter new phone number (or press Enter to keep {contact.phone}): ") or contact.phone
                new_email = input(f"Enter new email (or press Enter to keep {contact.email}): ") or contact.email
                new_address = input(f"Enter new address (or press Enter to keep {contact.address}): ") or contact.address
                contact.update_contact(new_name, new_phone, new_email, new_address)
                print("Contact updated successfully.")
                return
        print(f"No contact found with the name {name}.")

    def delete_contact(self):
        name = input("\nEnter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"No contact found with the name {name}.")

    def menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("\nExiting Contact Book.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
