class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        if contact.name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[contact.name] = contact
            print("Contact added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("Contact not found.")
    def show_contact(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for name in self.contacts:
                print(f"{name}: {self.contacts[name].phone}")

contact_book = ContactBook()

while True:
    print("\nContact Book Operations:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Show Contacts")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        contact = Contact(name, phone)
        contact_book.add_contact(contact)
    elif ch == 2:
        name = input("Enter contact name: ")
        contact_book.delete_contact(name)
    elif ch == 3:
        name = input("Enter contact name: ")
        contact_book.search_contact(name)
    elif ch == 4:
        contact_book.show_contact()
    elif ch == 5:
        break
    else:
        print("Invalid choice. Please try again.")