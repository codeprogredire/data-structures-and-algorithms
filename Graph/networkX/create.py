'''
Create a simple graph and display it. 
'''

import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_node(1)
g.add_node(2)

g.add_edge(2,5)
g.add_edge(4,1)

g.add_edges_from([(2,5),(2,3)])

print(nx.info(g))

nx.draw(g)

plt.show()

