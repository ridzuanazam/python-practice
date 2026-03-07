# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument to the decorator
#
#             Example : some people want an vinalla icecream and some want a vinalla icecream with sprinkles
#                       so decorator being used to change its behavior without changing the base function

#             @add_sprinkles
#             get_ice_cream("vinalla")

# basic formula to create a decorator:
#
# def add_sprinkles(func):
#     def wrapper():
#         func()
#     return wrapper

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("**You add Sprinkles 🎊**")
        func(*args, **kwargs) # ← print("Here is your ice cream 🍨 ")
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("**You add Fudge 🍫**")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨 ")

get_ice_cream("Mango")