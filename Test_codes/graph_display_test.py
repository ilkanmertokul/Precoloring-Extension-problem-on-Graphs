# 1801042649
# Ilkan Mert Okul

# THIS IS A TRAINING AREA FOR LEARNING GRAPH OPERATIONS ON networkx.
# WILL NOT BE IN FINAL PRODUCT.

import networkx as nx
import matplotlib.pyplot as plt

import graph_operations

# Standard graph

edges = [(1, 2), (2, 3), (3, 4), (4, 1), (4, 9)]  # Edges
graph = nx.Graph(edges)  # Initialize
print(f"Nodes: {graph.edges}\nEdges: {graph.nodes}\n\n--------------------\n")


# Graph with attributes

graph = nx.Graph()

graph.add_node(1, color=2)
graph.add_node(2, color=3)
graph.add_node(3, color=4)

graph.add_edges_from([(1, 2), (2, 3), (1, 3)])

print(f"Node 1: {graph.nodes[1]}")
print(f"Nodes: {graph.edges}\nEdges: {graph.nodes}\n\n--------------------\n")

# Graph drawing

g = graph_operations.GraphOperator(20, 0.2)
nx.draw_networkx(g.graph)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
plt.axis("off")
plt.show()

