# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local → Enclosed → Global → Built-in

# Local variable

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

# Enclosed variable

def func1():
    x = 1
    def func2():
        print(x)
    func2()

func1()

# Global variable

def func1():
    print(x)

def func2():
    print(x + 2)

x = 3

func1()
func2()

# Built-in variable

from math import e

def func1():
    print(e)

func1()