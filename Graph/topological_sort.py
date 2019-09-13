'''
Implementation of topological sorting for a directed acyclic graph (DAG).
'''

from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.graph=defaultdict(list)
        self.numVertex=numVertex
    
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def topologicalUtilityFunc(self,v,visited,stack):
        visited[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalUtilityFunc(i,visited,stack)
        
        # Insert the current node at the start of the stack. LIFO
        stack.insert(0,v)
    
    
    
    def topological_sort(self):
        visited=[False]*self.numVertex
        stack=[]

        for i in range(self.numVertex):
            if visited[i]==False:
                self.topologicalUtilityFunc(i,visited,stack)
            
        print('The topological ordering of the given DAG is : ',stack)


# Driver code

g= Graph(3) 
g.add_edge(0,1)
g.add_edge(1,2)

g.topological_sort()