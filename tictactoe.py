'''playing with AI'''
import numpy as np 
gc=0
def game(gc):
    x,c=np.full((3,3),' '),0
    def win(y): #checking for winner
        for i in range(3):
            j = list(set(y[:, i]))  # checking vertically
            if len(j) == 1 and j[0] != ' ':
                if j[0] == 'X': return 'player'
                else: return 'AI'
            j = list(set(y[i, :]))  # checking horizontally
            if len(j) == 1 and j[0] != ' ':
                if j[0] == 'X': return 'player'
                else: return 'AI'
        else:
            j = list(set(np.diag(y[::-1])))  # checking regular diagonal
            if len(j) == 1 and j[0] != ' ':
                if j[0] == 'X': return 'player'
                else: return 'AI'
            j = list(set(np.diag(y)))  # checking reverse diagonal
            if len(j) == 1 and j[0] != ' ':
                if j[0] == 'X':return 'player'
                else:return 'AI'
        return ''

    def AI():
        print('after AI turn...')
        if (gc%2!=0 and np.count_nonzero(x==' ')==9) or x[1][1]==' ':
            x[1][1]='O'
            return 
        for j in ('O','X'): #checking posibility for Ai to win else blocking player possibility to win
            for i in range(3):
                if np.count_nonzero(x[:,i] == j)==2 and np.count_nonzero(x[:,i]==' ')==1:
                    pos=np.where(x[:,i]==' ')[0][0]
                    x[pos][i]='O'
                    return 
                if np.count_nonzero(x[i,:] == j)==2 and np.count_nonzero(x[i,:]==' ')==1:
                    pos=np.where(x[i,:]==' ')[0][0]
                    x[i][pos]='O'
                    return 
            if np.count_nonzero(np.diag(x)==j)==2 and np.count_nonzero(np.diag(x)==' ')==1:
                pos=np.where(np.diag(x)==' ')[0][0]
                x[pos][pos]='O'
                return 
            if np.count_nonzero(np.diag(x[::-1])==j)==2 and np.count_nonzero(np.diag(x[::-1])==' ')==1:
                pos=np.where(np.diag(x[::-1])==' ')[0][0]
                x[2-pos][pos]='O'
                return 

        for i in range(3): #2 blank spaces case
            if np.count_nonzero(x[:,i] == 'X')==1 and np.count_nonzero(x[:,i]==' ')==2:
                pos=np.where(x[:,i]==' ')[0][0]
                x[pos][i]='O'
                return 
            if np.count_nonzero(x[i,:] == 'X')==1 and np.count_nonzero(x[i,:]==' ')==2:
                pos=np.where(x[i,:]==' ')[0][0]
                x[i][pos]='O'
                return
        
    def player(): #player playing...
        i = int(input('enter position(1-9): '))
        while x[(i-1)//3][(i-1)%3] != ' ': i=int(input('position occupied! enter another position number(1-9): '))
        x[(i-1)//3][(i-1)%3] = 'X'
        
    def display():
        for i in x: print(i)

    display()
    i=1
    while True:
        player() if gc%2==0 else AI()  
        c += 1
        display()
        if c > 4 and win(x): break
        if c == 9: break
        AI() if gc%2==0 else player()
        c += 1
        display()
        if c > 4 and win(x): break
    if c!=9: print(f'{win(x)} won') #printing the winner
    else: 
        if win(x): print(f'{win(x)} won')
        else: print('It\'s a tie ')
    ch=input('want to play again(y/n)?')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
game(gc)
