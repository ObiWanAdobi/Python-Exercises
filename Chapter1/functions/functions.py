print("Functions allow: \n better overview, maintainance, protection and protability and reusability of code \n")
print("Function Syntax: \n")
print("def functionName(Argument1, Argument2, and so on): \n \t Statemants \n")
print("Function that adds and prints two given integers")
def addFunct(a, b):
    print(str(a+b))
print("CallFunction addFunct(1,2) = ")
addFunct(1,2)
print("Use the Function to Subtract two values by just entering a minus number addFunct(1,-2)")
addFunct(1,-2)
print("Return value of a Function: store return in a variable and print that variable")
def getSomething():
    return "Hello World"
importantString = getSomething()
print(importantString)
print("use the return value directly in the print Statement:")
print(getSomething())

print("Get input from the user: Enter an Integer but if the user enters anything else than an integer the program will throw an exception and will ask the user to enter a number again")
numberCorrect = False
numb = 0
while(numberCorrect == False):
    try:
        numb = int(input("Please enter a Number: "))
        numberCorrect=True
    except:
        print("Sorry but that is not an correct Integer ")
        numberCorrect=False
print("Number Insertet is " + str(numb))    