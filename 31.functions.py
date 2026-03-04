# function = a block of resuable code place () after the function name to invoke it
# Arguments = any data send to function
# Parameter () = temporary varaible that used within a function
# return = statement used to end a function and send a result back to the caller

"""
def happy_birthday(name: str, age: int):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")
    print("Happy birthday to you!")

happy_birthday("Bro", 30)
"""

"""
def display_invoice(username: str, amount: float, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due date : {due_date}")

display_invoice("Joe", 100.2, "10/25")
"""

def add(x, y):
    z = x + y
    return z

z = add(4,6)

print(z)