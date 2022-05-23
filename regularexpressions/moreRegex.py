import re
#Case-Insensitive Matching parse second argument to re.copmile
    #re.I
caseInsensitiveSearch = re.compile(r'hello', re.I)
result = caseInsensitiveSearch.findall('Hello hello Hallo chello Halo hELLO HeLlo hElLo HEllo heLLo')
print(result)

#Search and replace Strings with the sub() Method
caseInsensitiveReplace = re.compile(r'Hello', re.I)
result2 = caseInsensitiveReplace.sub('Hello World', 'Hello hello Hallo chello Halo hELLO HeLlo hElLo HEllo heLLo')
print(result2)

justShowFirstLetter = re.compile(r'Agent (\w)\w*')
result3 = justShowFirstLetter.sub(r'\1****', 'My name is Agent Arno and this is my new name Agent Fkdfjasflkj3213123')
print(result3)

#Complex Regexes
    #Easier to read with argument: re.VERBOSE
    #ignores then whitespaces and comments inside the regular expression string

