from admin import Admin
from book import Book
from contact import Contact
from client import Client

class Library:
    def __init__(self):
        self.contacts = Contact()
        self.admins = Admin()
        self.clients = Client()
        self.books = Book()

    def get_library_contacts(self):
        return self.contacts.get_contacts()
    
    def add_library_contact(self, contact):
        self.contacts.add_contact(contact)

    def add_library_admin(self, username, password):
        self.admins.add_admin(username, password)

    def check_library_admin(self, username, password):
        return self.admins.check_admin(username, password)

    def add_library_book(self, title, author, genre, edition, publishing_company, purchase_price, selling_price):
        self.books.add_book(title, author, genre, edition, publishing_company, purchase_price, selling_price)
    
    def update_library_book(self, title, property, property_value):
        self.books.update_book(title, property, property_value)
    
    def find_library_book(self, property, property_value):
        return self.books.find_book(property, property_value)
    
    def remove_library_book(self, title):
        self.books.remove_book(title)
    
    def add_library_client(self, name, email):
        self.clients.add_client(name, email)
    
    def add_library_client_purchase(self, name, item_name, value):
        self.clients.add_new_purchase(name, item_name, value)

    def update_library_client(self, name, property, property_value):
        self.clients.update_client(name, property, property_value)
    
    def find_library_client(self, name):
        return self.clients.find_client(name)
    
    def remove_library_client(self, name):
        self.clients.remove_client(name)