import json
import time
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
from converter.trill_parser import load_trill
from converter.graph_utils import topological_order


def trill_to_notebook(trill_file, output_file="notebooks/generated_notebook.ipynb"):

    print("\n🚀 Starting Trill → Notebook conversion")

    start_time = time.time()

    # -------------------------------
    # Load workflow
    # -------------------------------
    nodes, edges = load_trill(trill_file)

    node_count = len(nodes)
    edge_count = len(edges)

    print(f"\n📊 Workflow statistics")
    print(f"Nodes detected: {node_count}")
    print(f"Edges detected: {edge_count}")

    # -------------------------------
    # Determine execution order
    # -------------------------------
    execution_order = topological_order(nodes, edges)

    print(f"\n🔗 Execution order:")
    print(execution_order)

    # -------------------------------
    # Convert node list → dictionary
    # (important for lookup)
    # -------------------------------
    node_dict = {node["id"]: node for node in nodes}

    # -------------------------------
    # Create notebook
    # -------------------------------
    nb = new_notebook()
    cells = []

    for node_id in execution_order:

        node = node_dict[node_id]

        code = node.get("code", "")

        if code.strip() == "":
            print(f"⚠️ Warning: Node {node_id} has no code")

        cells.append(new_code_cell(code))

    nb["cells"] = cells

    # -------------------------------
    # Save notebook
    # -------------------------------
    with open(output_file, "w") as f:
        nbformat.write(nb, f)

    end_time = time.time()
    conversion_time = end_time - start_time

    # -------------------------------
    # Final logs
    # -------------------------------
    print("\n✅ Conversion completed successfully!")

    print("\n📓 Notebook Summary")
    print(f"Cells created: {len(cells)}")
    print(f"Saved notebook: {output_file}")
    print(f"⏱ Conversion time: {conversion_time:.4f} seconds")

    print("\n✔ Validation checks")
    print(f"Nodes == Cells → {node_count == len(cells)}")

    if node_count != len(cells):
        print("⚠️ Warning: Node/cell mismatch detected")

    return output_file