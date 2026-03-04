# Python compound interest calculator

# FORMULA : A = P(1 + r/n)^t
# A : final amount
# P : initial principle balance
# r : interest rate
# t : number of time periods elapsed

principle = 0
rate = 0
time = 0
# 1st way
while principle <= 0:
    principle = float(input("Enter the principle amount: RM "))
    if principle <= 0:
        print("Principle can't be less or equal to zero.")
# 2nd way (same as 1st)
while True:
    rate = float(input("Enter rate : "))
    if rate <= 0:
        print("Rate can't be less or equal to zero.")
    else:
        break

while time <= 0:
    time = int(input("Enter time in year : "))
    if time <= 0:
        print("Time can't be less or equal to zero.")

print(f"Principle : RM {principle:^10.2f}")
print(f"Rate :         {rate:^10.2f}")
print(f"Year :         {time:^10}")

total = principle * pow((1 + rate / 100),time)

print(f"Balance after {time} {"year" if time == 1 else "years"} : RM {total:.2f}")