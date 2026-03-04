# while loop = execute some code WHILE some condition remains TRUE

"""
name = input("Enter your name: ")

while name == "":
    print("Please enter your name. ")
    name = input("Enter your name : ")

print(f"Welcome {name}")
"""

food = input("Enter the name of the FOOD to the list of menu(Enter 'q' to quit): ")

while not food == 'q':
    print(f"{food} now in the menu.")
    food = input("Enter the name of the FOOD to the list of menu(Enter 'q' to quit): ")

print("insert food to menu COMPLETED")
