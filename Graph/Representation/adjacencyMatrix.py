'''
A simple Graph representation using Adjacency matrix.
'''
class Graph:
    def __init__(self,numVertex):
        self.numVertex=numVertex
        self.adjMatrix=[[-1]*numVertex for _ in range(numVertex)]
        self.vertices={}
        self.verticeslist=[0]*numVertex
    
    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numVertex:
            self.vertices[id]=vtx
            self.verticeslist[vtx]=id
    
    def set_edge(self,frm,to,cost=0):
        frm=self.vertices[frm]
        to=self.vertices[to]
        self.adjMatrix[frm][to]=cost
        # For directed matrix, don't do this
        self.adjMatrix[to][frm]=cost
    
    def get_vertices(self):
        return self.verticeslist

    def get_edges(self):
        edges=[]
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                if self.adjMatrix[i][j]!=-1:
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        
        return edges
    
    def get_matrix(self):
        return self.adjMatrix

    def print_matrix(self):
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                print(self.adjMatrix[i][j],end=' ')
            print()