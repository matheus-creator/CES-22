from random import randint

def printPrettier():
    print()
    print('----------------------------')
    print()

class Document:
    def __init__(self, state, statement, author, expiresIn):
        self.statement = statement
        self.author = author
        self.expiresIn = expiresIn

        if state == 'draft':
            self.state = Draft(self)
        elif state == 'moderation':
            self.state = Moderation(self)
        else:
            self.state = Published(self)

    def render(self):
        self.state.render()

    def changeState(self, state):
        self.state = state

    def getDocumentStatement(self):
        return self.statement
    
    def documentAuthor(self):
        return self.author
    
    def documentValidUntil(self):
        return self.expiresIn

    def publish(self):
        self.state.publish()

class State:
    def __init__(self, document):
        self.document = document
        self.author = document.documentAuthor()

    def render(self):
        print(self.document.getDocumentStatement())

    def publish(self):
        pass

class Draft(State):
    def __init__(self, document):
        super().__init__(document)
    
    def render(self):
        super().render()
        print('Documento em construção.')
        printPrettier()
    
    def publish(self):
        super().publish()
        if (self.author == 'admin'):
            self.document.changeState(Published(self.document))
        else:
            self.document.changeState(Moderation(self.document))

class Moderation(State):
    def __init__(self, document):
        super().__init__(document)
    
    def render(self):
        super().render()
        print('Documento em revisão.')
        printPrettier()
    
    def publish(self):
        super().publish()
        situation = randint(0, 1)
        if situation == 1:
            self.document.changeState(Published(self.document))
            print('Documento aprovado.')
        else:
            self.document.changeState(Draft(self.document))
            print('Documento reprovado')


class Published(State):
    def __init__(self, document):
        super().__init__(document)
    
    def render(self):
        super().render()
        print('Documento publicado!')
        printPrettier()

    def publish(self):
        super().publish()
        if (self.document.documentValidUntil() < 0):
            self.document.changeState(Draft(self.document))
            

admin = 'admin'
member = 'member'

document = Document('draft', '"Meu novo documento."', member, 1)
#document = Document('draft', '"Meu novo documento."', admin, -1)

printPrettier()

document.render()
document.publish()
document.render()
document.publish()
document.render()
document.publish()
document.render()
document.publish()