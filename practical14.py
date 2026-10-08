from collections import Counter

phonebook = {}

while True:

    print("\n===== PHONEBOOK =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Word Frequency")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        phonebook[name] = phone

        print("Contact added successfully!")

    # DISPLAY CONTACTS
    elif choice == "2":
        print("\n--- CONTACTS ---")

        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            for name, phone in phonebook.items():
                print(name, ":", phone)

    # SEARCH CONTACT
    elif choice == "3":
        name = input("Enter name to search: ")

        if name in phonebook:
            print("Name:", name)
            print("Phone:", phonebook[name])
        else:
            print("Contact not found.")

    # UPDATE CONTACT
    elif choice == "4":
        name = input("Enter name to update: ")

        if name in phonebook:
            new_phone = input("Enter new phone number: ")

            phonebook[name] = new_phone

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # DELETE CONTACT
    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in phonebook:
            del phonebook[name]

            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # WORD FREQUENCY
    elif choice == "6":
        text = input("Enter a sentence: ")

        words = text.lower().split()

        count = Counter(words)

        print("\n--- WORD FREQUENCY ---")

        for word, frequency in count.items():
            print(word, ":", frequency)

    # EXIT
    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")