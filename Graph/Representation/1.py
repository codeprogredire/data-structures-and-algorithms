'''
Link: Adjacency matrix representation
'''

def addEdge(adjList,u,v):
    if adjList[u]==-1:
        adjList[u]=[v]
    else:
        adjList[u].append(v)
    if adjList[v]==-1:
        adjList[v]=[u]
    else:
        adjList[v].append(u)

def printGraph(adjList):
    V=len(adjList)

    for i in range(V):
        print('Adjacency list for vertex: %d \nhead'%i,end='')
        for x in adjList[i]:
            print('->%d'%x,end='')
        print()



if __name__=='__main__':
    V=5
    adj=[-1]*V

    addEdge(adj, 0, 1);
    addEdge(adj, 0, 4);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 1, 4);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);
    printGraph(adj);

