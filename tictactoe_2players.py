import numpy as np
x,c=[' ']*9,0
def win(x):
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

while True:
    i=int(input('player 1\'s turn(\'X\'): '))-1
    while x[i]!=' ':
        i=i=int(input('position occupied! enter another position number: '))-1
    x[i]='X'
    c+=1
    display()
    if c>4 and win(x):
        print(win(x))
        break
    if c==9:
        print('It\'s a Tie')
        break
    i=int(input('player 2\'s turn(\'X\'): '))-1
    while x[i]!=' ':
        i=i=int(input('position occupied! enter another position number: '))-1
    x[i]='O'
    c+=1
    display()
    if c>4 and win(x):
        print(win(x))
        break
