from random import randint

def printPrettier():
    '''
    Format output.
    '''
    print()
    print('----------------------------')
    print()


class Document:
    '''
    Class that represents a document.
    '''
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
        '''
        Render document.
        '''
        self.state.render()


    def changeState(self, state):
        '''
        Change document state.
        '''
        self.state = state


    def getDocumentStatement(self):
        '''
        Get document statement.
        '''
        return self.statement
    

    def documentAuthor(self):
        '''
        Get document author.
        '''
        return self.author
    

    def documentValidUntil(self):
        '''
        Get document validation.
        '''
        return self.expiresIn


    def publish(self):
        '''
        Publish document.
        '''
        self.state.publish()


class State:
    '''
    Class that represents a state.
    '''
    def __init__(self, document):
        self.document = document
        self.author = document.documentAuthor()


    def render(self):
        '''
        Render state.
        '''
        print(self.document.getDocumentStatement())


    def publish(self):
        '''
        Publish document, which depends on the current state.
        '''
        pass


class Draft(State):
    '''
    Class that represents the draft state.
    '''
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
    '''
    Class that represents the moderation state.
    '''
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
    '''
    Class that represents the published state.
    '''
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
            

# Choose the user type
user = 'member'
#user = 'admin'

# Change (>=0 for valid and <0, otherwise)
validUntil = -1

document = Document('draft', '"Meu novo documento."', user, validUntil)

printPrettier()

# Execute state transition
document.render()
document.publish()
document.render()
document.publish()
document.render()
document.publish()
document.render()
document.publish()