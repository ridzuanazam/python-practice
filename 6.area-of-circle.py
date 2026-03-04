import math

# fomula => A = pi*r²

radius = float(input("Enter the circle radius: "))

area = math.pi * pow(radius, 2)

print(f"The Area of the circle is : {round(area, 2)}cm²") # alt + 0178 = cm²