# Python Calculator

operator = input("Enter an operator (+ - * / ): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

result = ''

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print(f"{operator} is not valid operator")

if result:
    print(round(result, 3))