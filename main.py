import networkx as nx
import matplotlib.pyplot as plt

# Creates an undirected graph
G = nx.Graph()

# Adds nodes to the graph
G.add_nodes_from(["R1", "R2", "R3", "R4", "R5"])

# Adds weighted edges between all of the nodes in the graph
# Edge weights represent the cost of traveling between routers in the network
G.add_weighted_edges_from([("R1", "R2", 1), ("R1", "R3", 3), ("R1", "R4", 1),
                           ("R2", "R3", 4), ("R2", "R4", 2), ("R2", "R5", 10),
                           ("R3", "R4", 3), ("R3", "R5", 13),
                           ("R4", "R5", 5)])

print("Network Details:")
print("Routers:", G.nodes())
print("Paths:", G.edges())

for u, v, weight in G.edges.data("weight"):
    print(f"Edge: ({u}, {v}) weight: {weight}")

print()
# OSPF Simulation
# For each router, calculate the shortest path to all other routers
for source_router in G.nodes():
    print(f"OSPF Routing Table for {source_router}:")
    print("Dest | Next Hop | Cost")
    print("-" * 5 + "|" + "-" * 10 + "|" + "-" * 5)
    
    # Using Dijkstra's algorithm to find shortest paths and their lengths
    lengths, paths = nx.single_source_dijkstra(G, source_router)
    for destination_router in sorted(G.nodes()):
        if source_router == destination_router:
            print(f"{destination_router:^4} | {'--':^8} | {0:^4}")
        else:
            path = paths[destination_router]
            # The next hop is the second router in the path list
            next_hop = path[1] if len(path) > 1 else '--'
            cost = lengths[destination_router]
            print(f"{destination_router:^4} | {next_hop:^8} | {cost:^4}")

    print() # Add an empty line for separation between routing tables

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Network Graph")
plt.show()