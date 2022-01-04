'''playing tictactoe with AI'''
import numpy as np
x, v, c = [' ']*9, list(range(9)), 0
pos = {1: [(2, 3), (5, 9), (4, 7)], 2: [(1, 3), (5, 8)], 3: [(2, 1), (5, 7), (6, 9)], 4: [(1, 7), (5, 6)], 5: [
    (1, 9), (2, 8), (3, 7)], 6: [(3, 9), (5, 4)], 7: [(4, 1), (5, 3), (8, 9)], 8: [(7, 9), (5, 2)], 9: [(6, 3), (5, 1), (8, 7)]}

def display():
    for i in range(0, 9, 3): print(x[i:i+3])
        
def AI(x, i):
    for j in pos[i]:  # checking connected blocks
        if x[i-1] == x[j[0]-1]:
            if x[j[1]-1] == ' ':
                x[j[1]-1] = 'O'
                v.remove(j[1]-1)
                return x
        elif x[i-1] == x[j[1]-1]:
            if x[j[0]-1] == ' ':
                x[j[0]-1] = 'O'
                v.remove(j[0]-1)
                return x
    for j in pos[i]:  # filling connected empty blocks
        if x[j[0]-1] == ' ':
            x[j[0]-1] = 'O'
            v.remove(j[0]-1)
            return x
        elif x[j[1]-1] == ' ':
            x[j[1]-1] = 'O'
            v.remove(j[1]-1)
            return x
    x[v.pop()] = 'O'  # filling remained unconnected blocks
    return x

def win(y):
    y = np.resize(np.array(y), (3, 3))
    for i in range(3):
        j = list(set(y[:, i]))  # checking vertically
        if len(j) == 1 and j[0] != ' ':
            if j[0] == 'X': return 'player won'
            else: return 'AI won'
        j = list(set(y[i, :]))  # checking horizontally
        if len(j) == 1 and j[0] != ' ':
            if j[0] == 'X': return 'player won'
            else: return 'AI won'
    else:
        j = list(set(np.diag(y[::-1])))  # checking regular diagonal
        if len(j) == 1 and j[0] != ' ':
            if j[0] == 'X': return 'player won'
            else: return 'AI won'
        j = list(set(np.diag(y)))  # checking reverse diagonal
        if len(j) == 1 and j[0] != ' ':
            if j[0] == 'X':return 'player won'
            else:return 'AI won'
    return ''

display()
while True:
    i = int(input('enter position(1-9): '))
    while x[i-1] != ' ': i=int(input('position occupied! enter another position number(1-9): '))
    x[i-1] = 'X'
    v.remove(i-1)
    c += 1
    display()
    if c > 4 and win(x):
        print(win(x))
        break
    if c == 9:
        print('It\'s a tie ')
        break
    print('after AI turn...')
    if i != 5 and x[4] == ' ': x[4] = 'O'
    else: x = AI(x, i)
    c += 1
    display()
    if c > 4 and win(x):
        print(win(x))
        break
