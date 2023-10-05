class Node:
    def __init__(self, label):
        self.label = label
        self.inbound_links = []
        self.outbound_links = []

class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)
        self.nodes[from_node].outbound_links.append(to_node)
        self.nodes[to_node].inbound_links.append(from_node)

def identify_router(graph):
    max_connections = -1
    router_label = None

    for node_label, node in graph.nodes.items():
        total_connections = len(node.inbound_links) + len(node.outbound_links)
        if total_connections > max_connections:
            max_connections = total_connections
            router_label = node_label
        elif total_connections == max_connections:
            # Handle tie-breaking by choosing the smaller label
            router_label = min(router_label, node_label)
    return router_label

# Test cases
graph1 = DirectedGraph()
graph1.add_edge(1, 2)
graph1.add_edge(2, 3)
graph1.add_edge(3, 5)
graph1.add_edge(5, 2)
graph1.add_edge(2, 1)
result1 = identify_router(graph1)  # Should return 2

graph2 = DirectedGraph()
graph2.add_edge(1, 3)
graph2.add_edge(3, 5)
graph2.add_edge(5, 6)
graph2.add_edge(6, 4)
graph2.add_edge(4, 5)
graph2.add_edge(5, 2)
graph2.add_edge(2, 6)
result2 = identify_router(graph2)  # Should return 5

graph3 = DirectedGraph()
graph3.add_edge(2, 4)
graph3.add_edge(4, 6)
graph3.add_edge(6, 2)
graph3.add_edge(2, 5)
graph3.add_edge(5, 6)
result3 = identify_router(graph3)  # Should return 2

print(result1)  # Output: 2
print(result2)  # Output: 5
print(result3)  # Output: 2

# Explanation
# The time complexity is O(N), Where N is the number of node in the graph

# This is because the function iterates through 
# all nodes once to calculate the total connections for each node

# Each operation inside the loop (e.g., getting inbound and outbound links) 
# takes constant time as it involves dictionary lookups and list length 

# Therefore, the time complexity is linear with respect to the number of nodes in the graph.
