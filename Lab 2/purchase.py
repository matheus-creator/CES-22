class Purchase:
    '''
    Class that represents a purchase
    '''
    def __init__(self):
        self.products = []
        self.quantity = []
        self.values = []
    
    def add_item(self, name, value):
        if name not in self.products:
            self.products.append(name)
            self.values.append(value)
            self.quantity.append(1)
        else:
            index = self.products.index(name)
            self.quantity[index] += 1