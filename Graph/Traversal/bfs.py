'''
Breadth first Search Traversal of a graph.
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,start):
        queue=[start]
        visited=[start]

        while len(queue):
            item=queue.pop(0)
            print(item,end=' ')

            for i in self.graph[item]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)


# Driver code
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 