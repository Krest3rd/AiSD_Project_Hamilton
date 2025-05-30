from decoration import header, footer
from lists import Linked_List

def show_commands():
    header("AVAILABLE COMMANDS")
    print("""Print -\tprints the graph
Euler -\tfinds Euler cycle
Hamilton- finds Hamiltonian cycle
Help -\tdisplays this help message
Export - exports the graph to tikz
Exit -\texits the program""")
    footer()

def goodbye():
    header("Exiting the program...", pattern="-")

def print_graph(graph_data: list[Linked_List]) -> None:
    header("GRAPH")
    for node in graph_data:
        node.display()
    footer()


