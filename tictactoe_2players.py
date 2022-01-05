'''a python program to play tictactoe between 2 players (infinite times if they choose to)'''
import numpy as np
gc=0 #gamecount
def game(gc):
    x,c=[' ']*9,0
    def p(c): #player's function
        i=int(input(f'player {c}\'s turn: '))-1 #c variable is not global c. here c is used to determine which player is playing
        while x[i]!=' ': i=i=int(input('position occupied! enter another position number: '))-1
        x[i]='O' if c%2==0 else 'X'
        
    def display(): #for displaying the board
        for i in range(0,9,3): print(x[i:i+3])
    
    def win(x): #checking for winning
        x=np.resize(np.array(x),(3,3))
        for i in range(3):
                j=list(set(x[:,i])) #checking vertically
                if len(j)==1 and j[0]!=' ':
                    if j[0]=='X': return 'player 1'
                    else: return 'player 2'
                j=list(set(x[i,:])) #checking horizontally
                if len(j)==1 and j[0]!=' ':
                    if j[0]=='X': return 'player 1'
                    else: return 'player 2'
        else: #checking diagonals
            j=list(set(np.diag(x[::-1])))
            if len(j)==1 and j[0]!=' ':
                if j[0]=='X': return 'player 1'
                else: return 'player 2'
            j=list(set(np.diag(x)))
            if len(j)==1 and j[0]!=' ':
                if j[0]=='X': return 'player 1'
                else: return 'player 2'
        return ''
    
    display() #displaying the board in initial
    while True:
        p(1) if gc%2==0 else p(2) #roles will be reversed in next game
        c+=1
        display()
        if c>4 and win(x): break 
        if c==9: break #checking the Tie condition
        p(2) if gc%2==0 else p(1)
        c+=1
        display()
        if c>4 and win(x): break
    if c!=9: print(f'{win(x)} won') #to print who is the winner
    else: print('It\'s a Tie')
    ch=input('want to play again(y/n)? ')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
game(gc)
