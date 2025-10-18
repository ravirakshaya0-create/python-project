
contacts = {}

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"\n Contact '{name}' added successfully!")


def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")


def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")
    else:
        print(" No contact found with that name.")


def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name to update: ")
    if name in contacts:
        print("Leave blank if you don't want to change the field.")
        phone = input("New Phone Number: ")
        email = input("New Email: ")
        address = input("New Address: ")

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address

        print(f"\n Contact '{name}' updated successfully!")
    else:
        print(" Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑 Contact '{name}' deleted successfully!")
    else:
        print(" No contact found with that name.")


def main():
    while True:
        print("\n========= CONTACT BOOK =========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

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
            print("\n Thank you for using Contact Book!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")


main()