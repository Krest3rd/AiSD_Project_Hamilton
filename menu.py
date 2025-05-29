import sys
from generate import generate_hamiltonian_graph as generate_hamilton, calculate_nuber_of_edges as count_edges, generate_non_hamiltonian_graph as generate_non_hamilton
from commands import show_commands, print_graph, export_graph
from cycles import find_euler_cycle, find_hamilton_cycle
from lists import Linked_List


graph_data = None

def print_usage_and_exit():
    print("Correct usage: ./plik --hamilton OR ./plik --non-hamilton")
    sys.exit(1)

def prompt_graph_input(expect_saturation=False):
    try:
        nodes = int(input("nodes> ").strip())
        saturation = None
        if expect_saturation:
            saturation = int(input("saturation> ").strip())
        return nodes, saturation
    except ValueError:
        print("Invalid input. Please enter integers.")
        sys.exit(1)
    except EOFError:
        print("Ctrl+D detected. Exiting.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting.")
        sys.exit(1)
    
def command_handler():    
    while True:
        try:
            choice = input("action> ").strip().lower()
        except EOFError:
            print("Ctrl+D detected. Exiting.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting.")
            sys.exit(1)

        if choice == "help":
            show_commands()
        elif choice == "print":
            print_graph(graph_data)
        elif choice == "euler":
            print("Finding Euler cycle...")
            find_euler_cycle(graph_data)
        elif choice == "hamilton":
            print("Finding Hamilton cycle...")
            find_hamilton_cycle(graph_data)
        elif choice == "export":
            print("Exporting graph to TikZ...")
            export_graph(graph_data)
        elif choice == "exit":
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid command. Type 'help' for available commands.")

        

def generate_graph_mode(expect_saturation=True):
    print(f"=== {'' if expect_saturation else 'Non '}Hamilton Graph  ===")
    nodes, saturation = prompt_graph_input(expect_saturation)

    global graph_data
    if expect_saturation:
        graph_data = generate_hamilton(nodes, count_edges(nodes, saturation))
    else:
        graph_data = generate_non_hamilton(nodes, count_edges(nodes, 50))
    print(f"{'' if expect_saturation else 'Non '}Hamilton Graph generated!")

    command_handler()
