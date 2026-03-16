
Curio ↔ Jupyter Notebook Interoperability Prototype

Project structure:

data/
  workflow.json                 Sample Curio workflow
  generated_workflow.json       Output after notebook conversion

notebooks/
  example.ipynb                 Example notebook

converter/
  trill_parser.py               Reads Curio Trill JSON
  nb_to_trill.py                Converts notebook -> Trill
  graph_utils.py                Topological sorting

scripts/
  run_demo.py                   Demo runner

Install dependencies:

pip install nbformat networkx

Run demo:

python scripts/run_demo.py

Convert notebook → workflow:

python converter/nb_to_trill.py
