class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.publications = []

    def add_publication(self, publication):
        self.publications.append(publication)
    
    def get_publications(self):
        return self.publications

    def get_name(self):
        return self.name