import os
import pickle


# Class for a contact
class Contact:
    def __init__(self, name, email_id, phone_no, address):
        self.name = name
        self.email_id = email_id
        self.phone_no = phone_no
        self.address = address

    def __str__(self):
        return "Name:{0} \n Email Id:{1} \n Phone No. :{2} \n Address: {3} \n ".format(self.name, self.email_id,
                                                                                       self.phone_no, self.address)

    def change_email_id(self, email_id):
        self.email_id = email_id

    def change_name(self, name):
        self.name = name

    def change_phone_no(self, phone_no):
        self.phone_no = phone_no

    def change_address(self, address):
        self.address = address


def add_new_contact():
    contacts_file = open("contacts_file", "rb")
    is_file_empty = os.path.getsize("contacts_file") == 0
    if not is_file_empty:
        contacts_list = pickle.load(contacts_file)
    else:
        contacts_list = []
    try:
        contact = get_contact_data()
        contacts_file = open("contacts_file", "rb+")
        contacts_list.append(contact)
        print(contacts_list)
        pickle.dump(contacts_list, contacts_file)
        print("New Contact is added successfully")
    except KeyboardInterrupt:
        print("Contact could not be added")
    except EOFError:
        print("Contact could not be added")
    finally:
        contacts_file.close()


def get_contact_data():
    try:
        contact_name = input("\nEnter the name of the contact\n")
        contact_email_id = input("Enter the Email id of the contact\n")
        contact_phone = input("Enter the Contact number\n")
        contact_address = input("Enter the Address of the contact\n")
        contact = Contact(contact_name, contact_email_id, contact_phone, contact_address)
        return contact

    except KeyboardInterrupt as e:
        # Keyboard Interrupt , contact could not be added
        raise e

    except EOFError as e:
        # Reached end of the file. Contact count not be added
        raise e


def show_contacts():
    try:
        contacts_file = open("contacts_file", "rb")
        is_file_empty = os.path.getsize("contacts_file") == 0
        if not is_file_empty:
            contacts_list = pickle.load(contacts_file)
            for contact1 in range(len(contacts_list)):
                print()
                print(contacts_list[contact1])
        else:
            print("\nContacts Manager is empty\n")
            return
        contacts_file.close()
    except IOError:
        print("\nFile is not accessible")


def find_contact():
    contacts_file = open("contacts_file", "rb")
    is_file_empty = os.path.getsize("contacts_file") == 0
    if not is_file_empty:
        find_name = input("\nEnter the name of the contact to search\n")
        is_contact_found = False
        contacts_list = pickle.load(contacts_file)
        for contact1 in contacts_list:
            contact_name = contact1.name
            find_name = find_name.lower()
            contact_name = contact_name.lower()
            if contact_name == find_name:
                print(contact1)
                is_contact_found = True
                break
        if not is_contact_found:
            print("Searched Contact not found")
    else:
        print("\nContacts Manager is empty. Cannot search")
    contacts_file.close()


def delete_contact():
    contacts_file = open("contacts_file", "rb+")
    is_file_empty = os.path.getsize("contacts_file") == 0
    if not is_file_empty:
        name = input("\nEnter the contact name to delete\n")
        contacts_list = pickle.load(contacts_file)
        is_contact_deleted = False
        for i in range(0, len(contacts_list)):
            contact1 = contacts_list[i]
            if contact1.name == name:
                del contacts_list[i]
                is_contact_deleted = True
                print("\nContact is deleted successfully\n")
                contacts_file = open("contacts_file", "rb+")
                if len(contacts_list) == 0:
                    contacts_file.write(b'')
                else:
                    pickle.dump(contacts_list, contacts_file)
                break
        if not is_contact_deleted:
            print("\nContact not found with the searched name\n")

    else:
        print("\nContacts Manager is empty. Cannot delete contact")
    contacts_file.close()


def edit_contact():
    contacts_file = open("contacts_file", "rb")
    is_file_empty = os.path.getsize("contacts_file") == 0
    if not is_file_empty:
        name = input("\nPlease Enter the Name of the Contact to be edited\n")
        contacts_list = pickle.load(contacts_file)
        is_contact_edited = False
        for contact1 in contacts_list:
            if contact1.name == name:
                do_edits(contact1)
                contacts_file = open("contacts_file", "rb+")
                pickle.dump(contacts_list, contacts_file)
                is_contact_edited = True
                print("\nContact is edited successfully\n")
                break
        if not is_contact_edited:
            print("Contact not found")
    else:
        print("\nContacts Manager is empty. Cannot delete contact")
    contacts_file.close()


def do_edits(contact):
    try:
        while True:
            print("\nEnter 1 to edit Email id , 2 to edit Phone number, 3 to edit the Address and 4 to exit without "
                  "editing")
            ch = input()
            if ch == "1":
                new_email_id = input("\nEnter the new email address of the contact\n")
                contact.change_email_id(new_email_id)
                break
            elif ch == "2":
                new_phone_no = input("\nEnter the new phone number of the contact\n")
                contact.change_phone_no(new_phone_no)
                break
            elif ch == "3":
                new_address = input("\nEnter the new Address of the contact\n")
                contact.change_address(new_address)
                break
            else:
                print("Incorrect choice is made")
                break

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt error has occurred")

    except EOFError:
        print("\nEnd of the file error has occurred")
