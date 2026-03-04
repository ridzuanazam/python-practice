# concession stand program

menu = {"pizza" : 3.00,
        "nachos" : 4.500,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "soda" : 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.02f}")
print("-------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food):
        cart.append(food)
        print(f"{food} is added to the cart.")
    else:
        print(f"{food} is not in the menu. Please try again")

print("----------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(f"{cart.index(food)+1}. {food}")

print()
print(f"Total : ${total:.02f}")