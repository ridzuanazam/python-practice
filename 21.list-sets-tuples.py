# collection = single "variable" used to store multiple values
#   List = []   ordered and changable. Duplicates OK
#   Set  = {}   unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple= ()   ordered and unchangeable. Duplicates OK. FASTER
"""
fruits = ["appple", "orange", "banana", "coconut", "coconut"]

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("coconut")
fruits.insert(2, "durian")
fruits.sort(reverse=True)
fruits.reverse()

print(fruits.index("pineapple"))
print(fruits.count("pineapple"))

print(fruits)
"""

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

fruits.add("pineapple")
fruits.remove("orange")
fruits.pop()
fruits.clear()

print(fruits)