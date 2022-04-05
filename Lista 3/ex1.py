import abc

class Airplane:
    """
    Abstract class that represents an airplane
    """
    __metaclass__ = abc.ABCMeta

    default_velocity = 600

    @classmethod
    @abc.abstractmethod
    def get_average_velocity(cls):
        """
        Returns the average velocity of the airplane
        """
        return cls.default_velocity


class Boeing(Airplane):
    """
    Class that represents a boeing
    """
    default_eficiency = 5
    default_fuel = 1000

    def __init__(self, length, height, velocity):
        """
        Creates a boeing with lenght, height and velocity
        """
        self.lenght = length
        self.height = height
        self.velocity = velocity


    def get_average_velocity(self):
        """
        Implements the abstract method that returns the average velocity
        """
        return (self.velocity + super(Boeing, self).get_average_velocity()) / 2

    
    @classmethod
    def compute_max_autonomy(cls):
        """
        Returns the autonomy of the boeing
        """
        return cls.product(cls.default_eficiency, cls.default_fuel)


    @staticmethod
    def product(a, b):
        """
        Returns the product of two floats
        """
        return a * b


boeing787 = Boeing(57, 17, 700)
print(boeing787.get_average_velocity())
print(Boeing.compute_max_autonomy())