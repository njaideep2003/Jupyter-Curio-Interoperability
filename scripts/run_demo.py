import sys
import os
import time

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from converter.nb_to_trill import notebook_to_trill
from converter.trill_to_notebook import trill_to_notebook
from converter.trill_parser import load_trill
from converter.graph_utils import topological_order


print("\n🚀 Starting Curio ↔ Notebook interoperability demo\n")

start = time.time()

# -----------------------------------
# Step 1: Notebook → Trill JSON
# -----------------------------------

print("STEP 1: Converting Notebook → Trill JSON")

workflow = notebook_to_trill("notebooks/example.ipynb")

with open("data/generated_workflow.json", "w") as f:
    import json
    json.dump(workflow, f, indent=2)

print("✔ Notebook converted to Trill JSON")
print("Saved file: data/generated_workflow.json")


# -----------------------------------
# Step 2: Parse workflow
# -----------------------------------

print("\nSTEP 2: Parsing Trill workflow")

nodes, edges = load_trill("data/generated_workflow.json")

print("Nodes detected:", len(nodes))
print("Edges detected:", len(edges))


# -----------------------------------
# Step 3: Execution ordering
# -----------------------------------

print("\nSTEP 3: Determining execution order")

order = topological_order(nodes, edges)

print("Execution order:")
print(order)


# -----------------------------------
# Step 4: Trill JSON → Notebook
# -----------------------------------

print("\nSTEP 4: Converting Trill JSON → Notebook")

output_nb = trill_to_notebook("data/generated_workflow.json")

print("Notebook generated:", output_nb)


end = time.time()

print("\n------------------------------------")
print("🎉 Demo completed successfully")
print("------------------------------------")

print(f"\nTotal pipeline time: {end-start:.4f} seconds")