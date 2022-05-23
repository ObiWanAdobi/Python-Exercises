#Project on Page: 154
#passwordLocker.py - an insecure password locker program
    #program can be executed by: 
        #python3 ./passwordLocker.py InputName
        #Example: python3 ./passwordLocker.py blog
            #gives you the blog password what is saved in the program
    
#Step1: Program Design and Data Structures
PASSWORDS = {'email': 'asldfjalsdfjasldfj2342j348234kl', 
             'blog': 'asdlöfkjasdfj8123l123j9123!"3', 
             'luggage': '12345',
             'runescape': 'lel111'}

#Step2: Handle Command Line Arguments
import sys
    #need to import: pyperclip
if len(sys.argv) < 2: 
    print('usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

#sys.argv[0] is the name of the programm here it is passwordLocker.py
account = sys.argv[1] #first command line arg is the account name

#Step3: Copy the Right Password
if account in PASSWORDS: 
    #pyperclip.copy(PASSWORDS[account])
    print(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else: 
    print('There is no account named ' + account)
    print('\t Passwordes saved for these accounts: ')
    for a in PASSWORDS: 
        print(a)