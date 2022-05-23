


def commaCodeMaker(a):
    b = '\''
    for i in a:
        if i == a[-1]:
            b = b + "and " + str(i) + '\''
        else:
            b = b + str(i) + ", "
    return b

#Test 1: List with Strings
spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCodeMaker(spam))

#Test 2: List with Numbers. Needed to modify Function: added str() concat. works
numbList = []
for i in range(100):
    numbList.append(i)
print(commaCodeMaker(numbList))