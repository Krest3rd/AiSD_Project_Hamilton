def help():
    print("Available commands:")
    print("""
============= Commands ==============
Print -\tprints the graph
Euler -\tfinds Euler cycle
Hamilton- finds Hamilton cycle
Help -\tdisplays this help message
Export -\t exports the graph to tikz
Exit -\texits the program
=====================================
          """)

def print_graph(graph_data):
    print("========GRAPH=========")
    for node in graph_data:
        node.display()
    print("======================")
    