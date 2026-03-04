# Membership operators = used to test whether a value or a variable is found in a sequence 
#                        (string, list, tuple, set or dictionary) 
#                        1. in 
#                        2. not in
"""
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
"""

"""
students = {"Muhd", "Azam", "Ridzuan"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not in the list.")
else:
    print(f"{student} is in the list.")
"""

"""
grades = {"Muhd":'A', 
          "Azam":'B', 
          "Ridzuan":'C'}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found in the list.")
"""

email = "azamridzuan@gmail.com"

if "@" in email and "." in email:
    print(f"{email} was a valid email.")
else:
    print(f"{email} was not a valid email.")