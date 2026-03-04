# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. Phone, Book, Cup
#          You need a "class" to create many objects

# class = (blueprint) use to design the structure and layout of an object
"""
class Car:
    # create constructor
    # constructor is the method/function that will run when creating a new object
    # self → this object are being created right now
    def __init__(self, model: str, year: int, color: str, for_sale:bool):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
"""

from python_car_oop import Car
# Create an Object Car
car1 = Car("BMW", 2025, "Midnight Blue", True)
car2 = Car("Corvert", 2026, "Red", False)

print(car1.model, car1.year, car1.color, car1.for_sale, sep="\n")
print("----------------------------------------------------")
print(car2.model, car2.year, car2.color, car2.for_sale, sep="\n")
print("----------------------------------------------------")
print()
print("----------------")
car1.drive()
print("----------------")
car1.stop()
print("----------------")
car1.describe()
print("----------------")
car2.drive()
print("----------------")
car2.describe()