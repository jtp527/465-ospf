import networkx as nx
#import matplotlib.pyplot as plt

#Creates an undirected graph
G = nx.Graph()

#adds nodes to the graph
G.add_nodes_from(["R1", "R2", "R3", "R4", "R5"])

#adds weight edges between all of the nodes in the graph
#edge weights represent the cost of traveling between routers in the network
G.add_weighted_edges_from([("R1", "R2", 1), ("R1", "R3", 3), ("R1", "R4", 5), ("R1", "R4", 1),
                          ("R2", "R3", 4), ("R2", "R4", 2), ("R2", "R5", 10),
                          ("R3", "R4", 3), ("R3", "R5", 13),
                          ("R4", "R5", 5)])

#nx.draw(G, with_labels=True)

print("Routers:", G.nodes())
print("Paths:", G.edges())
#prints the relationship and weight between each node pair
for u, v, weight in G.edges.data("weight"): 
    print(f"Edge: ({u}, {v}) weight: {weight}")