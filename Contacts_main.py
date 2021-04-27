#!/usr/bin/python

from Contacts_Operations import *

print("\nWelcome to the Contacts Manager\n")

print("\nEnter 1 to Add new Contact, \n2 to Display All Contacts, \n3 to Delete existing Contact, \n4 to Edit a Contact, "
      "\n5 to Search for existing Contact and \n6 to Exit\n")

while True:
    ch = input("\nEnter your Option to proceed\n")
    if ch == '1':
        add_new_contact()
    elif ch == '2':
        show_contacts()
    elif ch == '3':
        delete_contact()
    elif ch == '4':
        edit_contact()
    elif ch == '5':
        find_contact()
    elif ch == '6':
        print("Thank You")
        exit()
    else:
        print("\nIncorrect Option is chosen. Please enter the correct option again\n")
