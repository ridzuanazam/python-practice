# Inheritance = Allow a class to inherit attributes and methods from another class
#               Help with code reuseability and extensibility
#               class Child(Parent) / class Sub(Super)

class Animal:
    def __init__(self, name: str = "Animal"):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog =  Dog("Khitmir")
cat = Cat("Oyen")
mouse = Mouse("Mickey")
haiwan = Cat()

print(dog.name, dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name, cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name, mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

print(haiwan.name, haiwan.is_alive)
haiwan.eat()
haiwan.sleep()
haiwan.speak()

