# super() = Function used in a child class to call a method from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,  color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius *  self.radius}cm")
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width *  self.width}cm")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width *  self.width / 2}cm")
        super().describe()


circle = Circle(color="red",filled= True,radius= 5)
square = Square(color="Blue", filled= False, width= 6)
triangle = Triangle(color="Yellow", filled= True, width=7, height=9)

print(circle.color)
print(circle.filled)
print(f"{circle.radius}cm")
circle.describe()
print()
print(square.color)
print(square.filled)
square.describe()
print(f"{square.width}cm")
print()
print(triangle.color)
print(triangle.filled)
triangle.describe()
print(f"{triangle.width}cm")
