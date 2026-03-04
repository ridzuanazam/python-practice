
from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    favourite_drink("Air Sirap")
    favourite_food("Nasi Lemak") # sometimes you want to borrow the function from others without run its main()
    print("Goodbye!")

if __name__ == '__main__':
    main()