class Vehicle:
    """
    Class that represents a vehicle
    """
    def drive(self):
        return "I'm driving a "

    
    def addMotor(self, newMotor):
        """
        Add a new motor to the vehicle
        """
        self.motor = newMotor
        print(newMotor.start())


class Car(Vehicle):
    """
    Class that represents a car
    """
    def drive(self):
        return Vehicle.drive(self) + "Car"


    def addMotor(self, newMotor):
        super().addMotor(newMotor)


class Truck(Vehicle):
    """
    Class that represents a truck
    """
    def drive(self):
        return Vehicle.drive(self) + "Truck"


    def addMotor(self, newMotor):
        super().addMotor(newMotor)


class Motorcycle(Vehicle):
    """
    Class that represents a motorcycle
    """
    def drive(self):
        return Vehicle.drive(self) + "Motorcycle"


    def addMotor(self, newMotor):
        super().addMotor(newMotor)


class Motor:
    """
    Class that represents a motor
    """
    def start(self):
        return "Starting "


class CombustionMotor(Motor):
    """
    Class that represents a combustion motor
    """
    def start(self):
        return Motor.start(self) + "Combustion Motor!"


class EletricMotor(Motor):
    """
    Class that represents an eletric motor
    """
    def start(self):
        return Motor.start(self) + "Eletric Motor!"


class HybridMotor(Motor):
    """
    Class that represents a hybrid motor
    """
    def start(self):
        return Motor.start(self) + "Eletric Motor!"


# Creating a car with eletric motor

car = Car()
car.addMotor(EletricMotor())
print(car.drive())