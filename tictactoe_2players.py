'''general 2 player tic tac toe game'''
import numpy as np
gc=0 #gamecount
def game(gc):
    x,c=[' ']*9,0
    def win(x): #checking for winning
        x=np.resize(np.array(x),(3,3))
        for i in range(3):
                j=list(set(x[:,i])) #checking vertically
                if len(j)==1 and j[0]!=' ':
                    if j[0]=='X': return 'player 1 won'
                    else: return 'player 2 won'
                j=list(set(x[i,:])) #checking horizontally
                if len(j)==1 and j[0]!=' ':
                    if j[0]=='X': return 'player 1 won'
                    else: return 'player 2 won'
        else: #checking diagonals
            j=list(set(np.diag(x[::-1])))
            if len(j)==1 and j[0]!=' ':
                if j[0]=='X': return 'player 1 won'
                else: return 'player 2 won'
            j=list(set(np.diag(x)))
            if len(j)==1 and j[0]!=' ':
                if j[0]=='X': return 'player 1 won'
                else: return 'player 2 won'
        return ''

    def display():
        for i in range(0,9,3): print(x[i:i+3])

    def p1(): #player1 function
        i=int(input('player 1\'s turn: '))-1
        while x[i]!=' ': i=i=int(input('position occupied! enter another position number: '))-1
        x[i]='X' if gc%2==0 else 'O'

    def p2(): #player2 function
        i=int(input('player 2\'s turn: '))-1
        while x[i]!=' ': i=i=int(input('position occupied! enter another position number: '))-1
        x[i]='O' if gc%2==0 else 'X'

    while True:
        p1() if gc%2==0 else p2() #roles will be reversed in next iteration
        c+=1
        display()
        if c>4 and win(x):
            if gc%2==0: print(win(x),' won')
            else:
                x='player 1' if win(x)=='player 2' else 'player 2'
                print(x,' won')
            break
        if c==9:
            print('It\'s a Tie')
            break
        p2() if gc%2==0 else p1()
        c+=1
        display()
        if c>4 and win(x):
            if gc%2==0: print(win(x),' won')
            else:
                x='player 1' if win(x)=='player 2' else 'player 2'
                print(x,' won')
            break
    ch=input('want to play again(y/n)? ')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
game(gc)
