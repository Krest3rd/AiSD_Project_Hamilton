import math
from copy import deepcopy
from decoration import header, footer,line,print_text_multiline

def show_commands():
    header("AVAILABLE COMMANDS")
    print("""Print -\tprints the graph
Euler -\tfinds Euler cycle
Hamilton- finds Hamilton cycle
Help -\tdisplays this help message
Export - exports the graph to tikz
Exit -\texits the program""")
    footer()

def goodbye():
    header("Exiting the program...", pattern="...")

def print_graph(graph_data):
    header("GRAPH")
    for node in graph_data:
        node.display()
    footer()

def find_euler_cycle(graph_data):
    
    n = len(graph_data)
    adjacency_dict = {i+1: [] for i in range(n)}
    for node, linked_list in enumerate(graph_data, start=1):
        current = linked_list.head
        while current:
            if current.data != node: 
                adjacency_dict[node].append(current.data)
            current = current.next

    # Check if all degrees are even - necessary condition for Euler cycle
    for node in adjacency_dict:
        if len(adjacency_dict[node]) % 2 != 0:
            header("EULER CYCLE NOT FOUND","\\!/")
            print("No Euler cycle: node", node, "has odd degree.")
            footer("\\!/")
            return
        
    stack = [1]
    path = []
    local_adj = deepcopy(adjacency_dict)

    while stack:
        vertex = stack[-1]
        if local_adj[vertex]:
            neighbour = local_adj[vertex].pop()
            local_adj[neighbour].remove(vertex)
            stack.append(neighbour)
        else:
            path.append(stack.pop())

    if len(path) == sum(len(neigh) for neigh in adjacency_dict.values()) // 2 + 1:
        header("EULER CYCLE FOUND")
        print("Euler cycle found:")
        line("-")
        print_text_multiline(path[::-1],width, path=True)
        footer()
    else:
        header("EULER CYCLE NOT FOUND","\\!/")
        print("Euler cycle not found (graph may be disconnected).")
        footer("\\!/")
def find_hamilton_cycle(graph_data):
    n = len(graph_data)
    path = [1]  

    def neighbors(vertex):
        current = graph_data[vertex-1].head
        while current:
            if current.data != vertex:  
                yield current.data
            current = current.next

    def backtrack(vertex, visited):
        if len(path) == n:
            # Check if there's an edge back to the start
            if path[0] in list(neighbors(vertex)):
                path.append(path[0])
                return True
            return False
        for neigh in neighbors(vertex):
            if neigh not in visited:
                visited.add(neigh)
                path.append(neigh)
                if backtrack(neigh, visited):
                    return True
                path.pop()
                visited.remove(neigh)
        return False

    visited = set([1])
    if backtrack(1, visited):
        header("HAMILTON CYCLE FOUND")
        print("Hamiltonian cycle found:")
        line("-")
        print_text_multiline(path,width, path=True)
        footer()
    else:
        header("HAMILTON CYCLE NOT FOUND","\\!/")
def export_to_tikz(graph_data, filename="graph_tikz.tex"):
    import math
    n = len(graph_data)
    radius = 3
    tikz_nodes = []
    tikz_edges = set()

    # Node style as in your Overleaf code
    node_style = "node/.style={circle, draw=blue!60, fill=blue!5, thick, minimum size=8mm}"
    edge_style = "edge/.style={-{Stealth[length=2mm]}, thick}"

    # Place nodes in a circle
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * round(math.cos(angle), 6)
        y = radius * round(math.sin(angle), 6)
        tikz_nodes.append(
            f"\\node[node] (v{i+1}) at ({x},{y}) {{{i+1}}};"
        )

    # Add directed edges (arrows)
    for i, linked_list in enumerate(graph_data, start=1):
        current = linked_list.head
        while current:
            a, b = i, current.data
            tikz_edges.add((a, b))
            current = current.next

    # Generate edge strings, using loops for self-loops
    tikz_edges_str = ""
    loop_styles = ["loop above", "loop right", "loop below", "loop left"]
    loop_count = 0
    for a, b in sorted(tikz_edges):
        if a == b:
            # Cycle through loop directions for variety
            loop_dir = loop_styles[loop_count % len(loop_styles)]
            tikz_edges_str += f"\\draw[edge, {loop_dir}] (v{a}) to (v{a});\n"
            loop_count += 1
        else:
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