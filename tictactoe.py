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
        if (gc%2!=0 and np.count_nonzero(x==' ')==9):
            x[1][1]='O'
            return 
        if x[1][1]==' ':
            x[1][1]='O'
            return 
        for j in ('O','X'):
            for i in range(3):
                if np.count_nonzero(x[:,i] == j)==2 and np.count_nonzero(x[:,i]==' ')==1:
                    pos=np.where(x[:,i]==' ')[0][0]
                    x[pos][i]='O'
                    print('1')
                    return 
                if np.count_nonzero(x[i,:] == j)==2 and np.count_nonzero(x[i,:]==' ')==1:
                    pos=np.where(x[i,:]==' ')[0][0]
                    x[i][pos]='O'
                    print('2')
                    return 
            if np.count_nonzero(np.diag(x)==j)==2 and np.count_nonzero(np.diag(x)==' ')==1:
                pos=np.where(np.diag(x)==' ')[0][0]
                x[pos][pos]='O'
                print('3')
                return 
            if np.count_nonzero(np.diag(x[::-1])==j)==2 and np.count_nonzero(np.diag(x[::-1])==' ')==1:
                pos=np.where(np.diag(x[::-1])==' ')[0][0]
                print('4')
                if pos==0: x[2][0]='O'
                elif pos==1: x[1][1]='O'
                else: x[0][2]='O'
                return 
        print('5')
        l=np.argwhere(x==' ')
        l=l[np.random.randint(0,len(l))]
        x[l[0]][l[1]]='O'
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
        if gc%2==0:player() 
        else: AI()  
        c += 1
        display()
        if c > 4 and win(x): break
        if c == 9: break
        if gc%2==0: AI() 
        else:player()
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
