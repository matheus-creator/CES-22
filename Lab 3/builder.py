class Director:
    def make(self, builder, size, flavor):
        builder.setSize(size)
        builder.setFlavor(flavor)

    def makeChocolateCake(self, builder):
        self.make(builder, 'Large', 'Chocolate')
    
    def makePineappleCake(self, builder):
        self.make(builder, 'Medium', 'Pineapple')

    def makeCornCake(self, builder):
        self.make(builder, 'Small', 'Corn')

class Cake:
    def __init__(self):
        self.flavor = ''
        self.size = ''
        self.type = ''

class Builder:
    def __init__(self):
        self.cake = Cake()

    def setSize(self, size):
        self.cake.size = size

    def setFlavor(self, flavor):
        self.cake.flavor = flavor

    def getGenericResult(self):
        print(self.cake.flavor)
        print(self.cake.size)
    

class WeddingBuilder(Builder):
    def __init__(self):
        super().__init__()
        self.cake.type = 'Wedding'

    def getResult(self):
        super().getGenericResult()
        print(self.cake.type)


class BirthdayBuilder(Builder):
    def __init__(self):
        super().__init__()
        self.cake.type = 'Birthday'

    def getResult(self):
        super().getGenericResult()
        print(self.cake.type)

class InformalBuilder(Builder):
    def __init__(self):
        super().__init__()
        self.cake.type = 'Informal'

    def getResult(self):
        super().getGenericResult()
        print(self.cake.type)


director = Director()
wedding_builder = WeddingBuilder()
director.makeChocolateCake(wedding_builder)

print('Your cake:')
print()

wedding_builder.getResult()