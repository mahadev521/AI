
class Puzzle:
    def __init__(self,puz):
        self.puz = puz
        self.par=None
        self.h=0
    def __eq__(self,other):
        return self.puz==other.puz
    def __hash__(self):
        return hash((str(self.puz)))
    def display(self,row,col):
        return '\n'.join([' '.join(self.puz[i:i+col]) for i in range(0,row*col,col)])
    def isgoal(self,goal):
        return self.puz==goal

def heur(mat,goal):
    return sum([1 for i in range(row*col) if mat[i]!=goal[i]])

def sucessors(state):
    mat=state.puz
    ind=mat.index('_')
    total=row*col
    children=[]
    if (ind+1)%col!=0:
        newmat=mat.copy()
        newmat[ind],newmat[ind+1]=newmat[ind+1],newmat[ind]
        newstate=Puzzle(newmat)
        newstate.par=state
        newstate.h=heur(newmat,goal)+state.h
        children.append(newstate)
    if (ind+1)%col!=1:
        newmat=mat.copy()
        newmat[ind],newmat[ind-1]=newmat[ind-1],newmat[ind]
        newstate=Puzzle(newmat)
        newstate.par=state
        newstate.h=heur(newmat,goal)+state.h
        children.append(newstate)
    if ind+col<=total-1:
        newmat=mat.copy()
        newmat[ind],newmat[ind+col]=newmat[ind+col],newmat[ind]
        newstate=Puzzle(newmat)
        newstate.par=state
        newstate.h=heur(newmat,goal)+state.h
        children.append(newstate)
    if ind-col>=0:
        newmat=mat.copy()
        newmat[ind],newmat[ind-col]=newmat[ind-col],newmat[ind]
        newstate=Puzzle(newmat)
        newstate.par=state
        newstate.h=heur(newmat,goal)+state.h
        children.append(newstate)
    return children


def bestfirstsearch(mat,goal):
    recordx=Puzzle(mat)
    if recordx.isgoal(goal): return recordx
    openlist=[recordx] #openlist is a list of states
    closed=set()
    while openlist:
        state = openlist.pop(0)
        if state.isgoal(goal): return state
        closed.add(state)
        children = sucessors(state)
        for i in children:
            if i not in closed: 
                openlist.append(i)
        openlist.sort(key=lambda y:y.h)
    return None
        
def display(solution,row,col):
    if solution:
        path = [solution.display(row,col)]
        par = solution.par #for parent tracking
        while par:
            path.append(par.display(row,col))
            par = par.par
        for i in path[::-1]: 
            print(f'{i}\n')
    else:
        print(f'there is no solution for this puzzle')


if __name__ == '__main__':
    mat=['_','8','1','7','2','3','6','4','5']
    # mat=['1','2','5','4','3','6','7','8','_'] #no sol
    # mat=['1','2','3','8','_','4','7','6','5'] #puzzle with no solution
    goal=['1','2','3','4','5','6','7','8','_']
    # mat=['4','1','3','_','2','5','7','8','6',]
    row=3
    col=3
    display(bestfirstsearch(mat,goal),row,col)
