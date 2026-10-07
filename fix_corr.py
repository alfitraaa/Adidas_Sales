import json

with open("Adidas_Sales_Analysis.ipynb", "r") as f:
    nb = json.load(f)

for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
         source_str = "".join(cell["source"])
         if "sns.heatmap(df_adidas.corr()" in source_str:
              # We need to compute corr only on numeric columns.
              for j, line in enumerate(cell["source"]):
                  if "sns.heatmap(df_adidas.corr()" in line:
                      cell["source"][j] = "sns.heatmap(df_adidas.corr(numeric_only=True), annot=True, cmap='bone')\n"
                      print(f"Fixed cell {i}")

with open("Adidas_Sales_Analysis.ipynb", "w") as f:
    json.dump(nb, f, indent=2)
