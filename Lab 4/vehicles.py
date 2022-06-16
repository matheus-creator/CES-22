class Vehicle:  
    def drive(self):
        return "I'm driving a "
    
    def addMotor(self, newMotor):
        self.motor = newMotor
        print(newMotor.start())

class Car(Vehicle):
    def drive(self):
        return Vehicle.drive(self) + "Car"

    def addMotor(self, newMotor):
        super().addMotor(newMotor)

class Truck(Vehicle):
    def drive(self):
        return Vehicle.drive(self) + "Truck"

    def addMotor(self, newMotor):
        super().addMotor(newMotor)

class Motorcycle(Vehicle):
    def drive(self):
        return Vehicle.drive(self) + "Motorcycle"

    def addMotor(self, newMotor):
        super().addMotor(newMotor)

class Motor:
    def start(self):
        return "Starting "

class CombustionMotor(Motor):
    def start(self):
        return Motor.start(self) + "Combustion Motor!"

class EletricMotor(Motor):
    def start(self):
        return Motor.start(self) + "Eletric Motor!"

class HybridMotor(Motor):
    def start(self):
        return Motor.start(self) + "Eletric Motor!"

car = Car()
car.addMotor(EletricMotor())
print(car.drive())