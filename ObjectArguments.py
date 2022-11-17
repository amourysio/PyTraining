class Car:

    color = None


class Motorcycle:

    color = None


def change_color(vehicle, color):

    vehicle.color = color


car1 = Car()
car2 = Car()
car3 = Car()
bike = Motorcycle()

print(bike.color)

change_color(car1,"Red")
change_color(car2,"White")
change_color(car3,"Blue")
change_color(bike,"Black")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike.color)