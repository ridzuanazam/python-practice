#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Kgs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Lbs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 2)} {unit}")