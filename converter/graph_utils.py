
import networkx as nx

def topological_order(nodes, edges):
    G = nx.DiGraph()

    for n in nodes:
        G.add_node(n["id"])

    for e in edges:
        G.add_edge(e["source"], e["target"])

    order = list(nx.topological_sort(G))
    return order

if __name__ == "__main__":
    nodes = [{"id":"1"},{"id":"2"},{"id":"3"}]
    edges = [{"source":"1","target":"2"},{"source":"2","target":"3"}]

    order = topological_order(nodes, edges)
    print("Execution order:", order)
