# Prevents a user from creating an object of that Class
# + compels a user to override abstract method in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have implementation

# abc is abstract class
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("Car stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("Motorcycle stopped")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

