globalVariable = "Global variable"


def myFunction():
    print("\ninside function")
    print(globalVariable)
    localVariable = "Local variable"
    print(localVariable)


myFunction()
print("\noutside function")
print(globalVariable)
# print(localVariable)

# ----------------------------------------

variable = "Global variable"


def myFunction():
    print("\ninside function")
    variable = "Local variable"
    print(variable)


myFunction()
print("\noutside function")
print(variable)
