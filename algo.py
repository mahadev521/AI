class Generalalgorithms:
    def __init__(self,graph,start,goal):
        self.graph=graph
        self.start=start
        self.goal=goal 
    
    def bfs(self):
        open=[self.start]
        closed=set()
        while open:
            node=open.pop(0)
            closed.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in closed:
                    closed.add(neighbor)
                    open.append(neighbor)
        print("BFS Graph traversal completed")
    
    def dfs(self):
        open=[self.start]
        closed=set()
        while open:
            node=open.pop()
            closed.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in closed:
                    closed.add(neighbor)
                    open.append(neighbor)
        print("DFS Graph traversal completed")  
    
    
    def dfid(self,depth):
        open=[(self.start,0)]
        closed=set()
        trav=[]
        while open:
            node=open.pop()
            dep=node[1]+1
            node=node[0]
            closed.add(node)
            if str(node) not in trav: trav.append(str(node))
            for neighbor in self.graph[node]:
                if neighbor not in closed:
                    closed.add((neighbor,dep))
                    open.append((neighbor,dep))
            open=list(filter(lambda x:x[1]<=depth,open))
        print(' '.join(trav),end=' ')
        print(f"DFID Graph traversal of depth {dep-1} completed")
    
    
if __name__ =='__main__':
    #graph={ 0:[1,2], 1:[2], 2:[0,3],3:[3]}
    #dfs(graph,'A')
    graph=Generalalgorithms({0:[1,2],1:[0,3],2:[3,4],3:[4],4:[0]},1,4)
    graph.bfs()
    graph.dfs()
    for i in range(4):
        graph.dfid(i)
