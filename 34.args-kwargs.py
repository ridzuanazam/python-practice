# *args     = allows you to pass multiple nen-key arguments (tuple)
# **kwargs  = allows you to pass multiple keyword arguments (dictionary)
#              *unpacking operator
#               1. positional, 2. default, 3. keyword, 4. ARBITRARY
"""
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    
display_name("Dr.", "Peter", "Parker", "a.k.a", "Spiderman")
"""

"""
def print_address(**kwargs):
    print(type(kwargs))
    print("-----KEYS-----")
    for key in kwargs.keys():
        print(key)
    print("----VALUES----")
    for value in kwargs.values():
        print(value)
    print("-----KEYS VALUES PAIR------")
    for key, value in kwargs.items():
        print(f"{key:10} : {value}")

print_address(street="Jln Mulberi",
              city="Port Dickson", 
              state="Negeri Sembilan", 
              zip="71000")
"""

def shipping_label(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)
    print("\n\n")
    for arg in args:
        print(arg, end=" ",)
    print("\n\n")
    for key, value in kwargs.items():
        print(f"{key:10} : {value}")

shipping_label("Dr.", "Strange", "The", "III", 
               Hero="Marvel",
               Age=30, 
               Gender="Male", 
               Wizard=True)