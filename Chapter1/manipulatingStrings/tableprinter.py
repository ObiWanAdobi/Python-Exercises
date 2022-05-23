

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


#repeat range operation how does this shit work????
someTxt = tableData[0:7]
print(someTxt)


def printTable(data):
    outputLine1 = " "
    outputLine2 = " "
    outputLine3 = " "
    outputLIne4 = " "
    for a in data:
        outputLine1 += a[0] + " "
        outputLine2 += a[1] + " "
        outputLine3 += a[2] + " "
        outputLIne4 += a[3] + " "

    print(outputLine1)
    print(outputLine2)
    print(outputLine3)
    print(outputLIne4)


printTable(tableData)