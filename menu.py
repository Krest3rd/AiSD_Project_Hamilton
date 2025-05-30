import sys
from generate import generate_hamiltonian_graph as generate_hamilton, calculate_nuber_of_edges as count_edges, generate_non_hamiltonian_graph as generate_non_hamilton
from commands_cycles import find_euler_cycle, find_hamilton_cycle
from commands_export import export_to_tikz
from commands_else import show_commands, print_graph, goodbye
from decoration import header
from invalid import invalid_command,invalid_input, invalid_eof, invalid_keyboard_interrupt, invalid_usage


graph_data = None


def prompt_graph_input(expect_saturation=False):
    while True:
        try:
            nodes = int(input("nodes> ").strip())
            if nodes <= 2 + (0 if expect_saturation else 1):
                raise ValueError
            saturation = None
            if expect_saturation:
                saturation = int(input("saturation> ").strip())
                if saturation < 0 or saturation > 100:
                    raise ValueError
                
            return nodes, saturation
        except ValueError:
            invalid_input(2 + (0 if expect_saturation else 1))
            continue
        except EOFError:
            invalid_eof()
            break
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            break

def command_handler():    
    while True:
        try:
            choice = input("action> ").strip().lower()
        except EOFError:
            invalid_eof()
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()

        if choice == "help":
            show_commands()
        elif choice == "print":
            print_graph(graph_data)
        elif choice == "euler":
            find_euler_cycle(graph_data)
        elif choice == "hamilton":
            find_hamilton_cycle(graph_data)
        elif choice == "export":
            export_to_tikz(graph_data)
        elif choice == "exit":
            goodbye()
            sys.exit(0)
        else:
            invalid_command()

        

def generate_graph_mode(expect_saturation=True):
    header(f"=== {'' if expect_saturation else 'Non '}Hamiltonian Graph  ===","-"),
    nodes, saturation = prompt_graph_input(expect_saturation)

    global graph_data
    if expect_saturation:
        graph_data = generate_hamilton(nodes, count_edges(nodes, saturation))
    else:
        graph_data = generate_non_hamilton(nodes, count_edges(nodes, 50))
    header(f"{'' if expect_saturation else 'Non '}Hamiltonian Graph generated!","-")

    command_handler()
