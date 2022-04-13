class Puzzle:
    def __init__(self,puz,par=None,h=0,g=0):
        self.puz = puz #puzzle matrix
        self.par=par #for parent
        self.h=h #f(x)
        self.g=g #g(x)
    def __eq__(self,other):
        return self.puz==other.puz
    def __hash__(self):
        return hash((str(self.puz)))
    def __str__(self):
        return '\n'.join([' '.join(self.puz[i:i+col]) for i in range(0,row*col,col)])
    def isgoal(self,goal):
        return self.puz==goal

def heur(mat,goal): #function to find heuristic
    return sum([1 for i in range(row*col) if mat[i]!=goal[i]])

def sucessors(state):
    mat=state.puz
    ind=mat.index('0')
    children=[]
    if (ind+1)%col!=0: #moving right
        newmat=mat.copy()
        newmat[ind],newmat[ind+1]=newmat[ind+1],newmat[ind]
        children.append(Puzzle(newmat,state,heur(newmat,goal),state.g+1))
    if (ind+1)%col!=1: #moving left
        newmat=mat.copy()
        newmat[ind],newmat[ind-1]=newmat[ind-1],newmat[ind]
        children.append(Puzzle(newmat,state,heur(newmat,goal),state.g+1))
    if ind+col<=(row*col)-1: #movind down
        newmat=mat.copy()
        newmat[ind],newmat[ind+col]=newmat[ind+col],newmat[ind]
        children.append(Puzzle(newmat,state,heur(newmat,goal),state.g+1))
    if ind-col>=0: #moving up
        newmat=mat.copy()
        newmat[ind],newmat[ind-col]=newmat[ind-col],newmat[ind]
        children.append(Puzzle(newmat,state,heur(newmat,goal),state.g+1))
    return children

def Astar(mat,goal):
    openlist=[Puzzle(mat)] #openlist is a list of states
    closed=set()
    while openlist:
        state = openlist.pop(0)
        if state.isgoal(goal): return state
        closed.add(state)
        children = sucessors(state)
        for i in children:
            if i not in closed: openlist.append(i)
        openlist.sort(key=lambda y:y.h+y.g)
    return None

def bandb(mat,goal):
    openlist=[Puzzle(mat)] #openlist is a list of states
    closed=set()
    while openlist:
        state = openlist.pop(0)
        if state.isgoal(goal): return state
        closed.add(state)
        children = sucessors(state)
        for i in children:
            if i not in closed: openlist.append(i)
        openlist.sort(key=lambda y:y.g)
    return None

def hill(mat,goal):
    openlist=[Puzzle(mat)] #openlist is a list of states
    closed=set()
    while openlist:
        state = openlist.pop(0)
        if state.isgoal(goal): return state
        closed.add(state)
        children = sucessors(state)
        temp=[]
        for i in children:
            if i not in closed: temp.append(i)
        temp.sort(key=lambda y:y.h)
        openlist=temp+openlist
    return None

def beam(mat,goal,width):
    openlist=[Puzzle(mat)] #openlist is a list of states
    closed=set()
    wopen=openlist[:width]
    openlist.clear()
    while wopen:
        for i in range(width):
            try:
                state = wopen.pop(0)
                if state.isgoal(goal): return state
                closed.add(state)
                children = sucessors(state)
                for i in children:
                    if i not in closed: openlist.append(i)
                openlist.sort(key=lambda y:y.h)
            except: break
        wopen=openlist[:width]
        openlist.clear()
    return None

def bestfirst(mat,goal):
    openlist=[Puzzle(mat)] #openlist is a list of states
    closed=set()
    while openlist:
        state = openlist.pop(0)
        if state.isgoal(goal): return state
        closed.add(state)
        children = sucessors(state)
        for i in children:
            if i not in closed: openlist.append(i)
        openlist.sort(key=lambda y:y.h)
    return None

def display(solution,row,col):
    if solution:
        path = [solution]
        par = solution.par #for parent tracking
        while par:
            path.append(par)
            par = par.par
        for i in path[::-1]: print(f'{i}\n')
    else: print(f'there is no solution for this puzzle')

if __name__ == '__main__':   
    mat=[input(f'enter {i+1}th pos: ') for i in range(9)]
    # mat=['0','8','1','7','2','3','6','4','5']
    # mat=['1','2','5','4','3','6','7','8','0'] #no sol
    # mat=['1','2','3','8','0','4','7','6','5'] #puzzle with no solution
    goal=['1','2','3','4','5','6','7','8','0']
#     mat=['4','1','3','0','2','5','7','8','6',]
    # mat=['1','5','3','2','8','4','6','0','7']
    row=3
    col=3
    print('1.Astar\n2.Branch and bound\n3.Hill climbing\n4.Beam search\n5.Bestfirst')
    ch=int(input('enter your choice: '))
    if ch==1:
        print('astar algorithm')
        display(Astar(mat,goal),row,col)
    elif ch==2:
        print('branch and bound algorithm')
        display(bandb(mat,goal),row,col)
    elif ch==3:
        print('hill climbing algorithm')
        display(hill(mat,goal),row,col)
    elif ch==4:
        print('beam search algorithm')
        wid=int(input('enter beam width: '))
        display(beam(mat,goal,wid),row,col)
    else:
        print('bestfirst algorithm')
        display(bestfirst(mat,goal),row,col)
