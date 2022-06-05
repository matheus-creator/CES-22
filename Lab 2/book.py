from author import Author
from product import Product

class Book(Product):
    def __init__(self):
        super().__init__()
        self.titles = []
        self.authors = []
        self.genres = []
        self.editions = []
        self.publishing_companies = []

    def add_book(self, title, author, genre, edition, publishing_company, purchase_price, selling_price):
        for i in range(len(self.authors)):
            if self.authors[i].get_name() == author[0]:
                self.authors.append(self.authors[i])
                self.authors[i].add_publication(title)
                break
        else:
            author = Author(author[0], author[1])
            author.add_publication(title)
            self.authors.append(author)

        self.titles.append(title)
        self.genres.append(genre)
        self.editions.append(edition)
        self.publishing_companies.append(publishing_company)
        self.purchase_prices.append(purchase_price)
        new_selling_price = self.taxCalculator.getTaxRate(genre, purchase_price, selling_price) + selling_price
        self.selling_prices.append(new_selling_price)
    
    def update_book(self, title, property, property_value):
        if title in self.titles:
            index = self.titles.index(title)
            if property == 'title':
                self.titles[index] = property_value
            elif property == 'author':
                self.authors[index] = property_value
            elif property == 'genre':
                self.genres[index] = property_value
            elif property == 'edition':
                self.editions[index] = property_value
            elif property == 'publishing_company':
                self.publishing_companies[index] = property_value
            elif property == 'purchase_price':
                self.purchase_prices[index] = property_value
        else:
            print()
            print('Livro não encontrado.')

    def find_book(self, property, property_value):
        if property == 'title':
            if property_value in self.titles:
                index = self.titles.index(property_value)
                print()
                self.print_book_information(index)
                return True, self.selling_prices[index]
            else:
                print()
                print('Livro não encontrado.')
                return False, None
        elif property == 'author':
            index = 0
            for i in range(len(self.authors)):
                if self.authors[i].get_name() == property_value:
                    index = i
                    break
            else:
                print()
                print('Autor não encontrado.')
                return False, None
            self.print_author_publications(index)
    
    def print_book_information(self, index):
        print()
        print('Título:', self.titles[index])
        print('Autor:', self.authors[index].get_name())
        print('Gênero:', self.genres[index])
        print('Edição:', self.editions[index])
        print('Editora:', self.publishing_companies[index])
        print('Preço de compra:', self.purchase_prices[index])
        print('Preço de venda:', self.selling_prices[index])
    
    def print_author_publications(self, index):
        publications = self.authors[index].get_publications()
        print()
        print('Publicações:')
        print()
        
        for i in publications:
            print('->', i)

    def remove_book(self, title):
        if title in self.titles:
            index = self.titles.index(title)
            self.titles.pop(index)
            self.authors.pop(index)
            self.genres.pop(index)
            self.editions.pop(index)
            self.publishing_companies.pop(index)
            self.purchase_prices.pop(index)
            self.selling_prices.pop(index)
        else:
            print('Livro não encontrado.')