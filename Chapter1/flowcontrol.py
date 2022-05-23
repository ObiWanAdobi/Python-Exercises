from sqlalchemy import false

a = True
b = True
print("Boolean Tables")
print("\n a and b")
print(str(a) +" and "+ str(b) + " = "+ str(a and b))
a = False
print(str(a) +" and "+ str(b) + " = "+ str(a and b))
b = False
print(str(a) +" and "+ str(b) + " = "+ str(a and b))
a = True
print(str(a) +" and "+ str(b) + " = "+ str(a and b))
print("\n a or b")
a = True
b = True
print(str(a) +" or "+ str(b) + " = "+ str(a or b))
a = False
print(str(a) +" or "+ str(b) + " = "+ str(a or b))
b = False
print(str(a) +" or "+ str(b) + " = "+ str(a or b))
a = True
print(str(a) +" or "+ str(b) + " = "+ str(a or b))
print("\n not a")
print(str(a) + " = " + str(a))
print("not " + str(a) + " = " + str(not a))
a = False
print("not " + str(a) + " = " + str(not a))
print("\n Evaluation of Boolean Equations")
print("(5 > 4) and (3==5) Evaluates to False")
print((5 > 4) and (3==5))
print("and so on...")

print("\n Coparison Operators")
print("<,<=,>,>=, ==, !=")
print("\n IF-Statement \n")
print("If Condition: \n \t ConditionTrueStatements \n else: \n \t ConditionFalseStatements \n")
spam = 1
if spam == 1:
    print("Hello")
else:
    print("not Hello")
spam = 0
if spam == 1:
    print("Hello")
else:
    print("not Hello")
print("\n Loop-Statements")
print("Break -> Breaks out of the loop. Break if i ==3 \n")
i = 0
while(i < 5):
    print("Value of i is " + str(i))
    i = i + 1
    if i == 3:
        break
print("Continue -> skips iteration but continues with the next one. Continue if i==3 \n")
i = 0
while(i < 5):
    print("Value of i is " + str(i))
    i = i + 1
    if i == 3:
        continue
print("When a program is stuck at an infinit loop it can be interrupted by: strg+c")
print("\n For Loop with Range Examples: \n")
print("for i in range(): \n \t Statements \n")
print("range([StartValue], EndValue-1 (because start value is per default = 0), [IncrementDecrementSteps]")
print("range(10) and ")
print("range(0, 10) and")
print("range(0,10,1) \n are all doing the same thing")
for i in range(0,10,1):
    print(str(i))
print("Count from 0 to -9")
for i in range(-1,-11,-1):
    print(str(i))

