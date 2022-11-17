# from OOP import Car
class Car:

    # class variable
    wheels = 4

    # instance of variable
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This car {self.model} driving")

    def stop(self):
        print(f"This car {self.model} stopped")
