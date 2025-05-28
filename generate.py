from lists import Linked_List
from random import shuffle,sample

def generate_hamiltonian_graph(n: int, count: int) -> list[Linked_List]:
    """
    Generate a Hamiltonian graph with n vertices and a saturation degree.
    
    :param n: Number of vertices in the graph
    :param count: Minimum number of edges
    :return: List of linked lists representing the adjacency list of the graph
    """
    if n <= 0 or count < 0:
        raise ValueError("Number of vertices must be positive and count must be non-negative.")
    
    # if saturation > 100:
    #     raise ValueError("Saturation degree cannot exceed 100%.")

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

    # Calculate how many fields in the upper triangle of matrix (excluding the main diag)
    # count = 0
    # for i in range(1,n):
    #     count += i

    # # Calculate how many fields have to be filled (always rounds down)
    # count = int(count * saturation/100)
    count -= n  # Subtract the n edges already created in the cycle
    if count < 0:
        count = 0  # No additional edges needed

    attempts = 0
    max_attempts = 10 * count if count > 0 else 1  # Prevent infinite loops

    while count > 0 and attempts < max_attempts:
        # Randomly pick three distinct nodes
        a,b,c = sample(range(n), 3)

        # Try to connect a-b, b-c, c-a if not already connected and not self-loops
        pairs = [(a, b), (b, c), (c, a)]
        added = 0

        if b in adjacency_dict[a] or b in adjacency_dict[c] or a in adjacency_dict[c] and a!= b!=c:
            attempts += 1
            continue

        for u, v in pairs:
            adjacency_dict[u].append(v)
            adjacency_dict[v].append(u)
            added += 1
            count -= 1
            # if count == 0:
            #     break
        
    # Turn the adjacency dictionary into a list of linked lists
    # Initialize the adjacency list
    adjacency_list = [Linked_List() for _ in range(n)]
    for i in range(1,n+1):
        adjacency_list[i-1].InsertAtEnd(i)

    # Fill the adjacency list with edges
    for i in range(n):
        adjacency_dict[i].sort() # Sort for nice looking output
        for neighbor in adjacency_dict[i]:
            adjacency_list[i].InsertAtEnd(neighbor + 1)
            
    return adjacency_list
    
for i in generate_hamiltonian_graph(10, 70):
    i.display()  # Display the generated Hamiltonian graph
