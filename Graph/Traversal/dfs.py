'''
Implementation of Depth First Search for a directed graph.
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    # Helper function of DFS function
    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v,end=' ')

        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    # DFS function
    def DFS(self,start):
        visited=[False]*len(self.graph)

        self.DFSUtil(start,visited)

# Driver code
g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)