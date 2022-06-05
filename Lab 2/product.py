from taxCalculator import TaxCalculator

class Product:
    def __init__(self):
        self.taxCalculator = TaxCalculator()
        self.identifications = []
        self.purchase_prices = []
        self.selling_prices = []

    def add_item(self, identification, purchase_price, selling_price):
        self.identifications.append(identification)
        self.purchase_prices.append(purchase_price)
        new_selling_price = self.taxCalculator.getTaxRate('', purchase_price, selling_price)
    
    def update_item(self, identification, property, property_value):
        if identification in self.identifications:
            index = self.identifications.index(identification)
            if property == 'identification':
                self.identification[index] = property_value
            elif property == 'purchase_price':
                self.purchase_prices[index] = property_value
        else:
            print()
            print('Item não encontrado.')

    def find_item(self, identification):
        if identification in self.identifications:
            index = self.identifications.index(identification)
            print()
            self.print_item_information(index)
        else:
            print()
            print('Item não encontrado.')
    
    def print_item_information(self, index):
        print()
        print('Identificação:', self.identifications[index])
        print('Preço de compra:', self.purchase_prices[index])
        print('Preço de venda:', self.selling_prices[index])

    def remove_item(self, identification):
        if identification in self.identifications:
            index = self.titles.index(identification)
            self.identifications.pop(index)
            self.purchase_prices.pop(index)
            self.selling_prices.pop(index)
        else:
            print('Item não encontrado.')