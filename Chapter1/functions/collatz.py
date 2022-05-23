
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(str(number))
        return number
    else:
        number = 3*number+1
        print(str(number))
        return number

#Collatz Test
for i in range(1,11):
    collatz(i)

validInput = False
while(validInput == False):
    try:
        inputNumb = int(input("Insert a integer: "))
        validInput = True
    except:
        print("Please insert a valid integer value!!!!")

#call collatz(inputNumber) until the input number is 1
while(collatz(inputNumb) != 1):
    inputNumb = collatz(inputNumb)


