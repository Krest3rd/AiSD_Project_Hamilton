import sys

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

def help():
    print("Available commands:")
    print("""
============= Commands ==============
Print -\tprints the graph
Export -\texports the graph to tikzpicture
Euler -\tfinds Euler cycle
Hamilton- finds Hamilton cycle
Help -\tdisplays this help message
Exit -\texits the program
=====================================
          """)
    command_handler()
    
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
            help()
        elif choice == "print":
            #placceholder for print functionality
            print("Printing the graph...")
        elif choice == "euler":
            #placeholder for Euler cycle functionality
            print("Finding Euler cycle...")
        elif choice == "hamilton":
            #placeholder for Hamilton cycle functionality
            print("Finding Hamilton cycle...")
        elif choice == "exit":
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid command. Type 'help' for available commands.")

        

def run_hamilton_mode():
    print("=== Hamilton Graph  ===")
    nodes, saturation = prompt_graph_input(expect_saturation=True)

    global graph_data
#    #graph_data = hamilton generation
    print("Hamilton Graph generated!")

    command_handler()

def run_non_hamilton_mode():
    print("=== Non-hamilton Graph ===")
    nodes, _ = prompt_graph_input(expect_saturation=False)

    global graph_data
#   graph_data = generate_non_hamilton_graph
    print("Non-gamilton Graph generated!")

    command_handler()
