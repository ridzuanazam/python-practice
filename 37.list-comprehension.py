# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [{return expression} for {value} in {iterable} if {condition}]

#                      For every {value} that is {iterable}, check the {condition} than do the {expression} to be return

# OLD WAY
"""
doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
"""

# FASTER WAY
"""
doubles = [ x*2 for x in range(1, 11)]
triples = [ y*3 for y in range(1, 11)]
squares = [ z*z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)
"""

"""
fruits = ["apple", "orange", "banana", "coconut"]
fruits_first_char = [fruit[0] for fruit in fruits]
fruits_capitalize = [fruit[0].upper() + fruit[1:] for fruit in fruits]
fruits = [fruit.upper() for fruit in fruits]

print(fruits_first_char)
print(fruits_capitalize)
print(fruits)
"""

"""
numbers = [1, -2, 3, -4, 5, -6, 8, 7, -9, 23, 24, 28]

positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 ]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
"""

grades = [85, 62, 95, 54, 42, 30, 66]
passing_grades = [grad for grad in grades if grad>=50]

print(passing_grades)
