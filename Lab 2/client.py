from purchase import Purchase

class Client:
    '''
    Class that represents a client of the library.
    '''
    def __init__(self):
        self.clients = []
        self.emails = []
        self.purchases = [[]]
    
    def add_client(self, name, email):
        if name not in self.clients:
            self.clients.append(name)
            self.emails.append(email)
    
    def update_client(self, name, property, property_value):
        if name in self.clients:
            index = self.clients.index(name)
            if property == 'name':
                self.clients[index] = property_value     
            elif property == 'email':
                self.emails[index] = property_value
        else:
            print()
            print('Cliente não encontrado.')
    
    def find_client(self, name):
        if name in self.clients:
            index = self.clients.index(name)
            print()
            print(self.clients[index])
            print(self.emails[index])
            return True
        else:
            print()
            print('Cliente não encontrado.')
            return False

    def remove_client(self, name):
        if name in self.clients:
            index = self.clients.index(name)
            self.clients.pop(index)
            self.emails.pop(index)
            if self.purchases != []:
                self.purchases.pop(index)
        else:
            print()
            print('Cliente não encontrado.')

    def add_new_purchase(self, name, item_name, value):
        index = self.clients.index(name)

        if self.purchases[index] == []:
            self.purchases[index] = Purchase()
        
        self.purchases[index].add_item(item_name, value)
        