import math

# formula => c = sqrt(a² + b²)

a = float(input("Enter the a value: "))
b = float(input("Enter the b value: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse value is c : {round(c, 2)} cm²")