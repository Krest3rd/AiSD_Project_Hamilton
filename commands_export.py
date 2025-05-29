from decoration import header, footer, line, print_text_multiline
import math
from lists import Linked_List


def export_to_tikz(graph_data, filename="graph_tikz.tex"):
    n = len(graph_data)
    radius = 3
    tikz_nodes = []
    tikz_edges = set()

    # Node style as in your Overleaf code
    node_style = "node/.style={circle, draw=blue!60, fill=blue!5, thick, minimum size=8mm}"
    edge_style = "edge/.style={thick}"

    # Place nodes in a circle
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * round(math.cos(angle), 6)
        y = radius * round(math.sin(angle), 6)
        tikz_nodes.append(
            f"\\node[node] (v{i+1}) at ({x},{y}) {{{i+1}}};"
        )

    # Add undirected edges, no self-loops, avoid duplicates
    for i, linked_list in enumerate(graph_data, start=1):
        current = linked_list.head
        while current:
            a, b = i, current.data
            if a < b:  # undirected, avoid double edges
                tikz_edges.add((a, b))
            current = current.next

    # Generate edge strings (no arrows, no self-loops)
    tikz_edges_str = ""
    for a, b in sorted(tikz_edges):
        tikz_edges_str += f"\\draw[edge] (v{a}) -- (v{b});\n"

    tikz_code = (
        "\\begin{tikzpicture}[\n"
        f"    {node_style},\n"
        f"    {edge_style}\n"
        "]\n"
        + "\n".join(tikz_nodes)
        + "\n"
        + tikz_edges_str
        + "\\end{tikzpicture}\n"
    )

    with open(filename, "w") as f:
        f.write(tikz_code)
    header(f"TikZ code exported to {filename}", pattern="-")