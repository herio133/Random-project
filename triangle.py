import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
# Add edges correctly
g.add_edges_from([("a", "b"), ("b", "c"), ("a", "c")])

pos = {'a': (0, 1), 'b': (1, 2), 'c': (2, 1)}
nx.draw(g, pos, with_labels=True, node_size=700, node_color='lightblue', font_color='black', edge_color='gray')
plt.show()
