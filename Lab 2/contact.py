class Contact:
    def __init__(self):
        self.contacts = []

    def get_contacts(self):
        return self.contacts
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def delete_contact(self, contact):
        self.contacts.remove(contact)