# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")

    if food.lower() == "q":
        break

    while True:
        price = float(input(f"Enter the price of a {food}: RM "))
        if price < 0 :
            print("Price can't be less than zero.\n")
        break

    foods.append(food)
    prices.append(price)

print("\n -------YOUR CART--------")



for x in range(len(foods)):
    print(f"{foods[x]:<10} : {prices[x]:>10.2f}")

for price in prices:
    total += price
    
print("-------------------------")
print(f"Total(RM)  : {total:>10.2f}")
print()
print(foods)
print(prices)