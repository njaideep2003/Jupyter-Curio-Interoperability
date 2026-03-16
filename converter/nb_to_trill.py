import nbformat
import json
import time


def notebook_to_trill(notebook_file, output_file="data/generated_workflow.json"):

    print("\n🚀 Starting Notebook → Trill JSON conversion")

    start_time = time.time()

    # Load notebook
    nb = nbformat.read(notebook_file, as_version=4)

    cells = nb.cells
    code_cells = [cell for cell in cells if cell.cell_type == "code"]

    print(f"\n📓 Notebook statistics")
    print(f"Total cells: {len(cells)}")
    print(f"Code cells detected: {len(code_cells)}")

    nodes = []
    edges = []

    # Create nodes
    for i, cell in enumerate(code_cells):

        node = {
            "id": str(i + 1),
            "type": "code",
            "code": cell.source
        }

        nodes.append(node)

        # Create edge to next cell
        if i < len(code_cells) - 1:
            edges.append({
                "source": str(i + 1),
                "target": str(i + 2)
            })

    workflow = {
        "nodes": nodes,
        "edges": edges
    }

    # Save workflow
    with open(output_file, "w") as f:
        json.dump(workflow, f, indent=2)

    end_time = time.time()
    conversion_time = end_time - start_time

    print("\n✅ Conversion completed successfully!")

    print("\n📊 Workflow summary")
    print(f"Nodes created: {len(nodes)}")
    print(f"Edges created: {len(edges)}")
    print(f"Saved workflow file: {output_file}")
    print(f"⏱ Conversion time: {conversion_time:.4f} seconds")

    print("\n✔ Validation checks")

    print(f"Code cells == Nodes → {len(code_cells) == len(nodes)}")
    print(f"Sequential edges correct → {len(edges) == len(nodes)-1 if len(nodes)>0 else True}")

    if len(nodes) == 0:
        print("⚠️ Warning: No executable cells found in notebook")

    return workflow