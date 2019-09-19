'''
Reads edge lists from file "edges.txt" and creates a graph and plot it.
'''

import networkx as nx
import matplotlib.pyplot as plt

g=nx.read_edgelist('edges.txt',create_using=nx.Graph(),nodetype=int)

print(nx.info(g))

nx.draw(g)

plt.show()