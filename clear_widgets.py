import nbformat

notebook_path = "rap_transformer_.ipynb"

with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)

# Remove widget metadata errors
if "widgets" in nb.metadata and "state" not in nb.metadata["widgets"]:
    del nb.metadata["widgets"]

with open(notebook_path, "w") as f:
    nbformat.write(nb, f)

print(" Notebook cleaned!")
