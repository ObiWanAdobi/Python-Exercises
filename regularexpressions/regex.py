#Finding Patterns of Text with Regular Expressions

    #\d = numeral 0 to 9
    #\d\d\d-\d\d\d-\d\d\d\d = is the same as the function isPhoneNumber()
    #\d{3}-\d{3}-\{4} = is the same as the previous regex Only shorter
        #\d{3} = means 3 times this \d so \d\d\d

#Creating Regex Objects
import re

# without the r it would be re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
    #r stands for raw String and it is much easier to insert \ into and so on..
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

mo = phoneNumRegex.search('My number is 4')
if mo == None:
    print("none found")
else:
    print('Phone number found: ' + mo.group())


#Another Example: More Pattern Matching with Regular Expressions
#Grouping with Parentheses 
    #Group the Regex like (\d\d\d)-(\d\d\d-\d\d\d\d)
                #so (\d\d\d) = 1 Group 
                #and (\d\d\d-\d\d\d\d) = 2 Group
                #can get acess the content of the group with mo.group(1), mo.group(2)

phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex2.search('My number is 415-555-4242.')
print('Phone number Group 1 (First Part) found: ' + mo.group(1))
print('Phone number Group 2 (Second Part) found: ' + mo.group(2))
print('Phone number Group All found: ' + mo.group(0))


group1, group2 = mo.groups()
print(group1)
print(group2)


#OR Matching with | (Pipe Symbol)
    #multiple Groupts with the Pipe: (a|b|c|d) means matches if a or b or c or d
orRegex = re.compile(r'a|b|c|d')
result1 = orRegex.findall('Arno a Bla c Dddd efgha abcd')
print(result1)

    #Another Example:
orRegex2 = re.compile(r'A(rno|rnold|no)')
result2 = orRegex2.search("Arno is walking down the stairs Arnold is waiting for Ano")
print("Found these Names in the Story: ")
print(result2.group())

#Optional Matching with ? (Question Mark)
    #? after a group makes the group optional for the result
    #? means = match zero or 1 group before the ? =zero or =1
optionalRegex3 = re.compile(r'(www)?.google.(com|de|at)')
result3 = optionalRegex3.findall("www.google.at and www.google.de and google.at and google.com guuugle.tv guuulol.com")

print(result3)


    #Another Example: Better Phone Numbers
phoneRegex = re.compile(r'(\d\d\d-)?\d{3}-\d{4}')
result4 = phoneRegex.search('123-555-1231 is a number and also 555-1231')
print(result4)

#Kleene Stern: 
    #* means = match zero or more (so group can be zero or n times that group) >=0

kleeneSternRegex = re.compile(r'\d(number)*\d')
result5 = kleeneSternRegex.search('2numbernumbernumber5')
print(result5.group())
result5 = kleeneSternRegex.search('22')
print(result5.group())
result5 = kleeneSternRegex.search('3number5')
print(result5.group())
print('------------')

#+ for One or more (at least one)
    #+ means = at least one (or more) >= 1
plusRegex = re.compile(r'\d(number)+\d')
result5 = plusRegex.search('2numbernumbernumber5')
print(result5.group())
result5 = plusRegex.search('22')
print("result is none")
result5 = plusRegex.search('3number5')
print(result5.group())


#Curly Brackets for Specific Repetition
    #(Bla){3} matches BlaBlaBla
    #(Bla){n} matches only n times Bla ... (n a natural number)

    #(Bla){Insert Range here}
    #(Bla){1,3} matches Bla and BlaBla and BlaBlaBla

    #(Bla){,3} matches 0 to 3
    #(bla){3,} matches 3 or more


#Greedy matching = longest possible match (per default)
#notGreedy = shortest possible match -> after curly set a ?
    #here ? has nothing todo with the ? above for the option search!!!


#Find All
    #Returns List of Found Matches (when no groups are defined)
        #Example: \d\d\d-\d\d\d, return is [123-124, 123-321]
    #Returns Tuples of Groups (each group one String when Groups are defined)
        #Example: (\d\d\d-)(\d\d\d) return is [(123,123), (124,321)]


#Character Classes: 
    #\d = Digit
    #\D = all that are not Digits
    #\w = word (letter, digit or underscore chracter) like thisExample4, Exampl1238_ 
    #\W = not word 
    #\s = space Characters like space, tab or newline chracter
    #\S = not space Characters

    #[0-5] is like (0|1|2|3|4|5)

#Example1:
classRegexExample1 = re.compile(r'\d+\s\w+')
result6 = classRegexExample1.findall('thisissomethex 1sadidfk_ 123123123 word_')
print(result6)


#use [] for own Character Classes
vowelRegex = re.compile(r'aeiouAEIOU')
result7 = vowelRegex.findall('robocop eats baby food. BABY FOOD')
print(result7)

    #Another Example: 
        #[a-zA-Z0-9]

    #Negate Chracter Classes with ^ right after the opening brackets
        #[^a-z] means match everything that is not a small character



#The Caret and Dollar Sign Chracters
    #^ Indicates that match must start with this
        #Example '^Hello' matches everything that starts with Hello
    #$ Indicates that match must end with this
        #Example: 'hello$' matches everyhting that ends with hello

#Wildcards Character the Dot .
    #any character except a newline

    #Example: (.*) = matches everything

#Matching Nwline
    #re.compile('.*', re.DOTALL)