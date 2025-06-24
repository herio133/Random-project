import matplotlib.pyplot as plt
import networkx as nx

# Define points
points = {
    'A': (0, 2),
    'B': (1, 2),
    'C': (2, 2),
    'D': (0, 1),
    'E': (1, 1),
    'F': (2, 1),
    'G': (0, 0),
    'H': (1, 0),
    'I': (2, 0)
}

# Define lines as groups of 3 collinear points
lines = [
    ('A', 'B', 'C'),  # Horizontal
    ('D', 'E', 'F'),
    ('G', 'H', 'I'),

    ('A', 'D', 'G'),  # Vertical
    ('B', 'E', 'H'),
    ('C', 'F', 'I'),

    ('A', 'E', 'I'),  # Diagonals
    ('B', 'F', 'G'),
    ('C', 'D', 'H'),
    ('C', 'E', 'G'),
    ('B', 'D', 'I'),
    ('A', 'F', 'H')
]

# Plotting
plt.figure(figsize=(6, 6))
G = nx.Graph()

# Add nodes (points)
for name, pos in points.items():
    G.add_node(name, pos=pos)

# Draw points
nx.draw_networkx_nodes(G, points, node_size=500, node_color='skyblue')
nx.draw_networkx_labels(G, points, font_size=12)

# Draw lines
for line in lines:
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            G.add_edge(line[i], line[j])

nx.draw_networkx_edges(G, points, width=1.5, edge_color='gray', alpha=0.6)

plt.title("Affine Plane of Order 3 (9 Points, 12 Lines)")
plt.axis('off')
plt.tight_layout()
plt.show()
