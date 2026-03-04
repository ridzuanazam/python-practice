# if __name__ == __main__: by adding this if statement → (this script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing

# Good Practice makes code more ( - modular,
#                                 - helps readerability,
#                                 - leaves no global variables,
#                                 - avoid unintended execution)

#   ex. library = Import library for funtionality
#                 When running library directly, display a help page
#               = You can import the library for its functionality but
#                 when you run the library it self it will display help page about that library

def main():
    # Your Program goes  here
    pass

if __name__ == '__main__':
    main()

# Refer folder example41 to see the used of it
# Dunder mean double underscore __