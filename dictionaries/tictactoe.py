
from requests import get


print("Welcome to the tic tac toe game :) \n")
print("Insert Position where to put X or O: tl, top mid = tm, top right = tr, middle left = ml and so on mm, mr, ll, lm, lr}")

test = {
    'tl': 'X', 'tm': 'O', 'tr': 'X',
    'ml': '', 'mm': 'O', 'mr': '', 
    'll': '', 'lm': '', 'lr': 'O'
    }


def printBoard(board):
    print(board['tl'] + '|' +  board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' +  board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' +  board['lm'] + '|' + board['lr'])

print('tl' + '|' + 'tm' + '|' + 'tr')
print('-+-+-')
print('ml' + '|' + 'mm' + '|' + 'mr')
print('-+-+-')
print('ll' + '|' + 'lm' + '|' + 'lr')
print()



def resetBoard(board):
    print('\n Resets the board: \n')
    for i in board:
        board[i] = ' '
    

def checkIfWon(board):
    if((board['tl'] == 'X' and board['tm'] == 'X' and board['tr'] == 'X') or 
       (board['ll'] == 'X' and board['lm'] == 'X' and board['lr'] == 'X') or 
       (board['ml'] == 'X' and board['mm'] == 'X' and board['mr'] == 'X') or 
       (board['tl'] == 'X' and board['mm'] == 'X' and board['lr'] == 'X') or 
       (board['ll'] == 'X' and board['mm'] == 'X' and board['tr'] == 'X') or
       (board['tl'] == 'X' and board['ml'] == 'X' and board['ll'] == 'X') or
       (board['tm'] == 'X' and board['mm'] == 'X' and board['lm'] == 'X') or
       (board['tr'] == 'X' and board['mr'] == 'X' and board['lr'] == 'X') or
       (board['tl'] == 'O' and board['tm'] == 'O' and board['tr'] == 'O') or
       (board['ml'] == 'O' and board['mm'] == 'O' and board['mr'] == 'O') or 
       (board['ll'] == 'O' and board['lm'] == 'O' and board['lr'] == 'O') or 
       (board['tl'] == 'O' and board['mm'] == 'O' and board['lr'] == 'O') or 
       (board['ll'] == 'O' and board['mm'] == 'O' and board['tr'] == 'O') or
       (board['tl'] == 'O' and board['ml'] == 'O' and board['ll'] == 'O') or
       (board['tm'] == 'O' and board['mm'] == 'O' and board['lm'] == 'O') or
       (board['tr'] == 'O' and board['mr'] == 'O' and board['lr'] == 'O')):
        return True
    else:
        return False

if checkIfWon(test):
    print("Player 1 with O hast won the game on Turn ")
else:
    print("not won")


player1 = "X"
player2 = "O"
turn = True

for i in test:
    test[i] = ' '

counter = 0

while(counter < 9):
    printBoard(test)
    if turn: 
        getPosition = input("Turn for O. Move on which space?")
        if test[getPosition] == 'O' or test[getPosition] == 'X':
            print("\n Place is not empty try again! \n")
        else:
            test[getPosition] = 'O'
            counter = counter + 1
            if checkIfWon(test):
                print("Player 1 with O hast won the game on Turn " + str(counter))
                printBoard(test)
                break
            turn = not turn
    else:
        getPosition = input("Turn for X. Move on which space?")
        if test[getPosition] == 'O' or test[getPosition] == 'X':
            print("\n Place is not empty try again! \n")
        else:
            test[getPosition] = 'X'
            counter = counter + 1
            if checkIfWon(test):
                print("Player 2 with X hast won the game on Turn " + str(counter))
                break
            turn = not turn

