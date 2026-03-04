# Dictionary = a collection of {key : value} pairs ordered and changeable. NO DUPLICATES.

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# to view all attribute and method abt the dictionary
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
"""
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exists")
"""

# capitals.update({"Malaysia": "Kuala Lumpur"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# print(capitals)

# keys = capitals.keys()
# print(keys)

# .keys() return key
"""
for key in capitals.keys():
    print(key, end=" ")
"""

# values = capitals.values()
# print(values)

# .values() return values of the keys
"""
for value in capitals.values():
    print(value)
"""

# items = capitals.items()
# print(items)

# .items() return an object of { key : value } pairs
for key, value in capitals.items():
    print(f"{key} : {value}")