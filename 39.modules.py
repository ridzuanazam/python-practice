# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reuseable seperate files

# __pycache__  = is a folder where Python stores compiled bytecode versions of your .py files.
#                Appear in imported module's folder.
#                These .pyc files allow Python to:
#                 🚀 Run faster (skip recompiling your file every time)
#                 💾 Cache module bytecode so imports are quicker
#                 ⚙️ Keep version‑specific compiled files (e.g., cpython-311 for Python 3.11)
 #                 This folder appears any time you import a Python module, 
 #                 whether it’s from a folder, package, or direct file import.


# print(help(modules))
# print(help(os)) or print(help(math)) 

"""
# import math module
import math
print(math.pi)
"""

"""
# import math module but rename it (best practice)
import math as m
print(m.pi)
"""

"""
# import specific method(function) or atribute(data) from the math module and use it directly without rename it
from math import pi
print(pi) 
"""

import modules_example39.modules_example39 as math_file

result = math_file.pi
print(result)

result = math_file.square(3)
print(result)

result = math_file.area(4)
print(result)

result = math_file.cube(5)
print(result)

result = math_file.circumference(6)
print(result)