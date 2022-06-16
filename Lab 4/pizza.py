class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Dough(PizzaComponent):
    cost = 0.0

class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + '' + PizzaComponent.getDescription(self)
    
class Pepperoni(Decorator):
    cost = 25.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Cheese(Decorator):
    cost = 10.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Catupiry(Decorator):
    cost = 15.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Egg(Decorator):
    cost = 10.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

cheeseEgg = Egg(Cheese(Dough()))
print(cheeseEgg.getDescription() + ": $" + str(cheeseEgg.getTotalCost()))

pepperoniCatupiry = Catupiry(Pepperoni(Dough()))
print(pepperoniCatupiry.getDescription() + ": $" + str(pepperoniCatupiry.getTotalCost()))