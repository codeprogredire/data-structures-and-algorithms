'''
A simple representation of graph using Adjacency List.
'''

# Class to represent node of an Adjacency list
class AdjNode:
    def __init__(self,data):
        self.vertex=data
        self.next=None

class Graph:
    def __init__(self,numVertex):
        self.numVertex=numVertex
        self.adjList=[None]*numVertex

    # Function to add an edge in an undirected graph
    def add_edge(self,src,dest):
        # Adding the destination node to the source node
        node=AdjNode(dest)
        node.next=self.adjList[src]
        self.adjList[src]=node

        # Adding source node to destination as it is undirected graph
        node=AdjNode(src)
        node.next=self.adjList[dest]
        self.adjList[dest]=node

    def print_graph(self):
        for i in range(self.numVertex):
            print('Adjacency List of vertex {}\nhead'.format(i),end='')
            temp=self.adjList[i]
            while temp:
                print(' -> {}'.format(temp.vertex),end='')
                temp=temp.next
            print()