
import json

def load_trill(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data["nodes"], data["edges"]

def print_workflow(nodes, edges):
    print("Nodes:")
    for n in nodes:
        print(f"{n['id']} ({n['type']})")

    print("\nEdges:")
    for e in edges:
        print(f"{e['source']} -> {e['target']}")

if __name__ == "__main__":
    nodes, edges = load_trill("../data/workflow.json")
    print_workflow(nodes, edges)
