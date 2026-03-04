# Type of Str Method: can search str method using : help(str)
# result = len(name) # return length of name
# result = name.find("o") # return -1 if dont found, return the index number of that char
# result = name.capitalize() # return CAPITALIZED string
# result = name.upper # return uppercase string
# result = name.lower # return lowercase string
# result = name.isdigits # return True if string only digits
# result = name.isalpha # return True if string only alphabert
# result = phone_number.count("-") return total of "-"
# result = phone_number.replace("-", " ") return string replace the "-" with " " (spaces)


# Validate user input exercise
# 1. username is no more than 12 characters
# 2. usernmae must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1: # return -1 if not found any spaces
    print("Your username must not contain spaces")
elif not username.isalpha(): # return a bool = True if var contain alphabetic only
    print("Your username must not contain digits")
else:
    print(f"Welcome {username}")