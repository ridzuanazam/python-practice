# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Statics methods = Best for general utility functions that do not need access to class data (belong to a class not to any object created from that class)


class Employee:

    def __init__(self, name, posistion):
        self.name = name
        self.position = posistion

    # get_info is an instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Janitor", "Chef"]
        return position in valid_position
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Salleh", "Cashier")
employee3 = Employee("Mat", "   Chef")

# Static Method Print out
print(Employee.is_valid_position("Chef"))
# Instance Method Print out
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())