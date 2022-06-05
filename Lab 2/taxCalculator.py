class TaxCalculator:
    '''
    Class to calculate taxes of products
    '''
    def getTaxRate(self, genre, purchase_price, selling_price):
        new_genre = genre.lower()
        tax = 0.5
        if new_genre == 'mistério':
            tax = 0.6
        elif new_genre == 'romance':
            tax = 0.8
        elif new_genre == 'terror':
            tax = 0.4
        elif new_genre == 'drama':
            tax = 0.3
        return tax * (selling_price - purchase_price)