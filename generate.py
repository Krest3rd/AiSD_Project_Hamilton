from lists import Linked_List
from random import shuffle

def generate_hamiltonian_graph(n: int, saturation: int) -> list[Linked_List]:
    """
    Generate a Hamiltonian graph with n vertices and a saturation degree.
    
    :param n: Number of vertices in the graph
    :param saturation: Degree of saturation for the edges
    :return: List of linked lists representing the adjacency list of the graph
    """
    if n <= 0 or saturation < 0:
        raise ValueError("Number of vertices must be positive and saturation must be non-negative.")
    
    if saturation > 100:
        raise ValueError("Saturation degree cannot exceed 100%.")

    adjacency_dict = {i: [] for i in range(0, n)}

    # Create hamiltonian cycle
    T = [i for i in range(0, n)]


    # Generate a single cycle permutation (Hamiltonian cycle)
    T = [i for i in range(n)]
    shuffle(T)
    # Ensure it's a single cycle: connect T[i] to T[(i+1)%n]
    for i in range(n):
        adjacency_dict[T[i]].append(T[(i + 1) % n])
        adjacency_dict[T[(i + 1) % n]].append(T[i])

    # # Initialize the adjacency list
    # adjacency_list = [Linked_List() for _ in range(n)]
    # for i in range(1,n+1):
    #     adjacency_list[i-1].InsertAtEnd(i)

    
generate_hamiltonian_graph(10, 70)  # Example usage
