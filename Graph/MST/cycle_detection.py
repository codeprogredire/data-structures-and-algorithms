'''
Code to detect cycle in a directed graph.
'''

from collections import defaultdict

class Graph:
    def __init__(self,numVertices):
        self.numVertices=numVertices
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    # Helper function of isCyclic
    def isCyclicUtil(self,v,visited,recStack):
        visited[v]=True
        recStack[v]=True

        for neighbour in self.graph[v]:
            if visited[neighbour]==False:
                if self.isCyclicUtil(neighbour,visited,recStack)==True:
                    return True
            elif recStack[neighbour]==True:
                return True
        
        recStack[v]=False
        return False
    
    # Function to detect cycle in a graph
    def isCyclic(self):
        visited=[False]*self.numVertices
        recStack=[False]*self.numVertices

        for node in range(self.numVertices):
            if visited[node]==False:
                if self.isCyclicUtil(node,visited,recStack)==True:
                    return True
        
        return False


# Driver Code
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic(): 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")