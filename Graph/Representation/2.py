'''
Link: Adjacency matrix representation
'''
def addEdge(adjMat,u,v):
    adj[u][v]=1
    adj[v][u]=1

def printGraph(adj):
    V=len(adj)

    for i in range(V):
        for j in range(V):
            print(adj[i][j],end=' ')
        print()



if __name__=='__main__':
    V=5
    adj=[]
    for i in range(V):
        temp=[]
        for j in range(V):
            temp.append(0)
        adj.append(temp)

    addEdge(adj, 0, 1);
    addEdge(adj, 0, 4);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 1, 4);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);
    printGraph(adj);


