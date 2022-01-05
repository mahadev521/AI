import numpy as np
gc=0
def game(gc):
    x,a,c = [' ']*9,[], 0
    pos = {1: [(2, 3), (5, 9), (4, 7)], 
           2: [(1, 3), (5, 8)], 
           3: [(2, 1), (5, 7), (6, 9)], 
           4: [(1, 7), (5, 6)], 
           5: [(1, 9), (2, 8), (3, 7)], 
           6: [(3, 9), (5, 4)], 
           7: [(4, 1), (5, 3), (8, 9)], 
           8: [(7, 9), (5, 2)], 
           9: [(6, 3), (5, 1), (8, 7)]}
    
    def display(): #displaying the board
        for i in range(0, 9, 3): print(x[i:i+3])
    
    def player(): #player playing...
        i = int(input('enter position(1-9): '))
        while x[i-1] != ' ': i=int(input('position occupied! enter another position number(1-9): '))
        x[i-1] = 'X'
        return i
            
    def AI(x, i): #Ai playing...
        print('after AI turn...')
        if i != 5 and x[4] == ' ': 
            x[4] = 'O'
            a.append(4)
        else:
            for j in pos[i]:  # checking connected blocks of player and blocking his next move
                if x[i-1] == x[j[0]-1]:
                    if x[j[1]-1] == ' ':
                        x[j[1]-1] = 'O'
                        a.append(j[1]-1)
                        return x
                elif x[i-1] == x[j[1]-1]:
                    if x[j[0]-1] == ' ':
                        x[j[0]-1] = 'O'
                        a.append(j[0]-1)
                        return x

            for k in a:
                for j in pos[k]:  # filling connected empty blocks, chance of ai winning
                    if x[i-1] == x[j[0]-1]:
                        if x[j[1]-1] == ' ':
                            x[j[1]-1] = 'O'
                            a.append(j[1]-1)
                            return x
                    elif x[i-1] == x[j[1]-1]:
                        if x[j[0]-1] == ' ':
                            x[j[0]-1] = 'O'
                            a.append(j[0]-1)
                            return x

            for j in pos[i]:  # filling non connected empty blocks
                    if x[j[0]-1] == ' ':
                        x[j[0]-1] = 'O'
                        return x
                    elif x[j[1]-1] == ' ':
                        x[j[1]-1] = 'O'
                        return x

    def win(y): #checking for winner
        y = np.resize(np.array(y), (3, 3))
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

    display()
    while True:
        i=player() if gc%2==0 else AI(x,1)  
        c += 1
        display()
        if c > 4 and win(x): break
        if c == 9: break
        AI(x, i) if gc%2==0 else player()
        c += 1
        display()
        if c > 4 and win(x): break
    if c!=9: print(win(x)) #printing the winner
    else: print('It\'s a tie ')
    ch=input('want to play again(y/n)?')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
game(gc)
