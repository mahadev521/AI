# 8 1 6
# 3 5 7
# 4 9 2
from itertools import combinations
po={1:8,2:1,3:6,4:3,5:5,6:7,7:4,8:9,9:2}
place={8:0,1:1,6:2,3:3,5:4,7:5,4:6,9:7,2:8}
x,c=[' ']*9,0
p,a=[],[]

def win(x): #checking for winner
    print(a)
    for i in combinations(a,2):
        tem=15-(po[i[0]]+po[i[1]])
        print('xxxx',place[tem])
        if 10>tem>0 and x[place[tem]]=='O': 
            return 'AI'
    for i in combinations(p,2):
        tem=15-(po[i[0]]+po[i[1]])
        if 10>tem>0 and x[place[tem]]=='X' and place[tem]!=5: 
            return 'Player'

def display():
    for i in range(0,9,3): print(x[i:i+3])




def AI():
    print('after AI turn.... ')
    if x[4]==' ':
        x[4]='O'
        a.append(5)
        return
    if c>2:
        for i in combinations(a,2):
            print(i)
            tem=15-(po[i[0]]+po[i[1]])
            if 10>tem>0 and x[place[tem]]==' ':
                x[place[tem]]='O'
                a.append(place[tem]+1)
                return
        else:
            for i in combinations(p,2):
                print(i)
                tem=15-(po[i[0]]+po[i[1]])
                if 10>tem>0 and x[place[tem]]==' ':
                    x[place[tem]]='O'
                    a.append(place[tem]+1)
                    return
    te=x.index(' ')
    x[te]='O'
    a.append(te+1)
    return



display()
while True:
    i=int(input('enter postion: '))-1
    while x[i]!=' ':i=int(input('position occupied! enter another position number: '))-1
    x[i]='X'
    p.append(i+1)
    c+=1
    display()
    if c>4 and win(x): break
    if c==9: break
    AI()
    c+=1
    display()
    if c>4 and win(x): break
if c!=9: print(f'{win(x)} won') #to print who is the winner
else: print('It\'s a Tie')
print(x)








