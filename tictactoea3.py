'''using approach 3(magic square) method'''
# 8 1 6
# 3 5 7
# 4 9 2

from itertools import combinations
po={1:8,2:1,3:6,4:3,5:5,6:7,7:4,8:9,9:2} #referencing
place={8:0,1:1,6:2,3:3,5:4,7:5,4:6,9:7,2:8} #dereferencing
gc=0 #to determine who should play first

def game(gc):
    x,c,p,a=[' ']*9,0,[],[]

    def win(x): #checking for winner
        for i in combinations(a,2):
            tem=15-(po[i[0]]+po[i[1]])
            if 10>tem>0 and x[place[tem]]=='O' and tem!=po[i[0]] and tem!=po[i[1]]:return 'AI'
        for i in combinations(p,2):
            tem=15-(po[i[0]]+po[i[1]])
            if 10>tem>0 and x[place[tem]]=='X' and tem!=po[i[0]] and tem!=po[i[1]]:return 'Player'

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
                tem=15-(po[i[0]]+po[i[1]])
                if 10>tem>0 and x[place[tem]]==' ':
                    x[place[tem]]='O'
                    a.append(place[tem]+1)
                    return
            else:
                for i in combinations(p,2):
                    tem=15-(po[i[0]]+po[i[1]])
                    if 10>tem>0 and x[place[tem]]==' ':
                        x[place[tem]]='O'
                        a.append(place[tem]+1)
                        return
        te=x.index(' ')
        x[te]='O'
        a.append(te+1)
        return

    def player():
        i=int(input('enter postion: '))-1
        while x[i]!=' ':i=int(input('position occupied! enter another position number: '))-1
        x[i]='X'
        p.append(i+1)
        
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
    if c!=9: print(f'{win(x)} won') #to print who is the winner
    else: print('It\'s a Tie')
    ch=input('want to play again(y/n)?')
    if ch=='y' or ch=='Y':
        gc+=1
        game(gc)
        
if __name__=='__main__':
    game(gc)
