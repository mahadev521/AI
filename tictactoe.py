'''using AI (approach 2)'''
import numpy as np 
gc=0
def game(gc):
    x,c=np.full((3,3),' '),0
    def win(y): #checking for winner
        for i in range(3):
            if "".join(y[:,i])=='XXX' or "".join(y[i,:])=='XXX': return 'player'
            elif "".join(y[:,i])=='OOO' or "".join(y[i,:])=='OOO': return 'AI'
        if "".join(np.diag(y[::-1]))=='XXX' or "".join(np.diag(y))=='XXX': return 'player'
        elif "".join(np.diag(y[::-1]))=='OOO' or "".join(np.diag(y))=='OOO': return 'AI'
        return ''
 
    def AI():
        print('after AI turn...')
        if  x[1][1]==' ':
            x[1][1]='O'
            return
        if c>2:
            for k in range(1,3):
                l=2 if k==1 else 1
                for j in ('O','X'): #checking posibility for computer to win else blocking player possibility to win
                    for i in range(3):
                        if np.count_nonzero(x[:,i] == j)==l and np.count_nonzero(x[:,i]==' ')==k:
                            pos=np.where(x[:,i]==' ')[0][0]
                            x[pos][i]='O'
                            return 
                        if np.count_nonzero(x[i,:] == j)==l and np.count_nonzero(x[i,:]==' ')==k:
                            pos=np.where(x[i,:]==' ')[0][0]
                            x[i][pos]='O'
                            return 
                    if np.count_nonzero(np.diag(x)==j)==l and np.count_nonzero(np.diag(x)==' ')==k:
                        pos=np.where(np.diag(x)==' ')[0][0]
                        x[pos][pos]='O'
                        return 
                    if np.count_nonzero(np.diag(x[::-1])==j)==l and np.count_nonzero(np.diag(x[::-1])==' ')==k:
                        pos=np.where(np.diag(x[::-1])==' ')[0][0]
                        x[2-pos][pos]='O'
                        return 
        i,j=np.argwhere(x==' ')[0]
        x[i][j]='O'
        
    def player(): #player playing...
        i = int(input('enter position(1-9): '))
        while x[(i-1)//3][(i-1)%3] != ' ': i=int(input('position occupied! enter another position number(1-9): '))
        x[(i-1)//3][(i-1)%3] = 'X'
        
    def display():
        for i in x: print(i)

    display()
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
    else: print('It\'s a tie ')
    ch=input('want to play again(y/n)?')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
if __name__=='__main__':
    game(gc)
