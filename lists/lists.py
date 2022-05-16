from copy import copy


a = ['a','b','c','d']
b = [123,456,789]
print(a)
print(b)
a.append('Hello')
a.remove('a')
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
print("[] used for Lists")
print("{} used for Sets")
print("() used for Tupels")
t = (12,13,45,78)
print(t)
print(t.index(12))
print(t.index(13))
print(t.index(45))
print(t.index(78))

def copyList(a):
    b = a.copy()
    return b

c = copyList(b)
print(c)

def modifysListDirect(a):
    print(a)
    a.pop()
    a.append("Hello World")
    print(a)

modifysListDirect(c)

d = [123,"hello"]
print(d)


spam = [2,4,6,8,10]
copyspam = []
for a in spam:
    if a == 6:
        copyspam.append("hello")
    copyspam.append(a)
print(copyspam)

spam[2] = "Hello"
print(str(spam[int(int('3'*2) / 11)]))
#'3'*2 eval to 33/11 eval to 3
#spam[3] eval to 8
print(spam[-1]) #gets the last element. Under 0 starts from behind
print(spam[-2])
print("spam[range]")
print(spam[:2]) #range(2) = 0 1

bacon = [3.14, 'cat', 11, 'cat', True]
print(str(bacon.index('cat'))) # index = 1

bacon.remove('cat')
print(bacon) # removes first instance of cat in the list

bacon.append(99) 
print(bacon)

print("Concat lists with + and replicate with * (exactly the same with strings)")
print(bacon+spam)
print(spam*3)

print("append(value) = adds value to the end of the list")
bacon.append("appendedValue")
print("insert(index, value) = adds value before the given index")
bacon.insert(0,"insertetAtIndex0")
print(bacon)

print(tuple(bacon))
print(list(t))
