import pytest
from Contacts_Operations import *


def test_add_new_contact():
    assert add_new_contact() == "new_contact_added"


def test_show_contacts():
    assert show_contacts() == "displayed"


def test_find():
    contacts_file = open("contacts_file", "rb")
    contacts_list = pickle.load(contacts_file)
    find_name = "Ash"
    is_contact_found = False
    assert find(contacts_list,find_name,is_contact_found) != "not_found"
    contacts_file.close()
