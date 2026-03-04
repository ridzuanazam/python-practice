# if = Do some code only IF the conditional is TRUE, ELSE do smth else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

online = True

if online:
    print("The user is Online")
else:
    print("The user is Offline")