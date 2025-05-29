from lists import Linked_List
import math

def show_commands():
    print("Available commands:")
    print("""
============= Commands ==============
Print -\tprints the graph
Euler -\tfinds Euler cycle
Hamilton- finds Hamilton cycle
Help -\tdisplays this help message
Export - exports the graph to tikz
Exit -\texits the program
=====================================
          """)

def print_graph(graph: list[Linked_List]) -> None:
    """Prints the graph in a readable format."""
    print("\n========GRAPH=========")
    for node in graph:
        node.display()
    print("======================\n")


def export_graph(graph: list[Linked_List]) -> None:
    """Exports the graph to a TikZ picture format."""

    """Generate a label for a node based on its index."""
    def get_node_label(index):
            # Use chr(65+i) to get letters A, B, C, ... AA, AB, ...
            label = ""
            while index >= 0:
                label = chr(65 + (index % 26)) + label
                index = index // 26 - 1
            return label
    
    print("\n========EXPORT========")
    positions = calculate_circle_positions(len(graph))
    
    result = "\\begin{scope}[every node/.style={circle,thick,draw}]\n"

    for i in range(len(graph)):
        label = get_node_label(i)
        result += f"\t\\node ({label}) at ({positions[i][0]},{positions[i][1]}) {{{i+1}}};\n"
    
    result += "\\end{scope}\n\n"
    
    result += "\\begin{scope}[every edge/.style={thick}]\n"
    for i,j in enumerate(graph):
        current = j.head.next
        while current is not None:
            label = get_node_label(i)
            current_label = get_node_label(current.data - 1)
            result += f"\t\\draw ({label}) -- ({current_label});\n"
            current = current.next
    
    result += "\\end{scope}\n"
    
    print(result)
    print("======================\n")


def calculate_circle_positions(n: int, radius: int = 5) -> list[tuple[float, float]]:
    """Calculate positions of n points evenly spread around a circle."""
    positions = [
        (
            radius * math.cos(2 * math.pi * i / n),
            radius * math.sin(2 * math.pi * i / n)
        )
        for i in range(n)
    ]
    return positions