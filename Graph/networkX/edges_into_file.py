'''
Write edges information into file "edge_info.txt"
'''

import networkx as nx

g=nx.Graph()

g.add_edges_from([(1,2),(3,4),(1,4)])

nx.write_edgelist(g,'edge_info.txt')