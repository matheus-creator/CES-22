class PizzaComponent:
    """
    Class that represents a pizza
    """
    def getDescription(self):
        """
        Returns the name of the class
        """
        return self.__class__.__name__


    def getTotalCost(self):
        """
        Returns the cost of the class that represents an ingredient of pizza
        """
        return self.__class__.cost


class Dough(PizzaComponent):
    """
    Class that represents a pizza's dough
    """
    cost = 0.0


class Decorator(PizzaComponent):
    """
    Abstract class for a pizza decorator
    """
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent
    

    def getTotalCost(self):
        """
        Returns the cost of the decorator plus the cost of the decorated
        """
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    

    def getDescription(self):
        """
        Returns the description of the decorator plus the description of the decorated
        """
        return self.component.getDescription() + '' + PizzaComponent.getDescription(self)
    

class Pepperoni(Decorator):
    """
    Decorator for pepperoni ingredient
    """
    cost = 25.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Cheese(Decorator):
    """
    Decorator for cheese ingredient
    """
    cost = 10.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Catupiry(Decorator):
    """
    Decorator for catupiry ingredient
    """
    cost = 15.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Egg(Decorator):
    """
    Decorator for egg ingredient
    """
    cost = 10.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


# Creating a pizza with cheese and eggs

cheeseEgg = Egg(Cheese(Dough()))
print(cheeseEgg.getDescription() + ": $" + str(cheeseEgg.getTotalCost()))

# Creating a pizza with pepperoni and catupiry

pepperoniCatupiry = Catupiry(Pepperoni(Dough()))
print(pepperoniCatupiry.getDescription() + ": $" + str(pepperoniCatupiry.getTotalCost()))