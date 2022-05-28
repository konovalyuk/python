try:
    divisionByZero = 7 / 0
    print(divisionByZero)
except:
    print("Error happened")

# ---------------------------------

try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter a number: "))
    variable = userInput1 / userInput2
    print("The result of division is ", variable)
    myFile = open("python_lesson.txt", 'r')
except ValueError:
    print("Error: you didn't enter a number")
except ZeroDivisionError:
    print("Error: division by zero")
except Exception as e:
    print("General error:", e)
