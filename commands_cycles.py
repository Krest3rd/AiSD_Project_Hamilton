from lists import Linked_List
from copy import deepcopy
from decoration import header, footer, line, print_text_multiline

def find_euler_cycle(graph_data: list[Linked_List]) -> None:
    """
    Find an Euler cycle in the given graph represented as a list of linked lists.

    :param graph_data: List of Linked_List objects representing the adjacency list of the graph.
    :return: None (prints the Euler cycle if found, otherwise indicates failure).
    """
    
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
        print_text_multiline(path[::-1], path=True)
        footer()
    else:
        header("EULER CYCLE NOT FOUND","\\!/")
        print("Euler cycle not found (graph may be disconnected).")
        footer("\\!/")


def find_hamilton_cycle(graph_data: list[Linked_List]) -> None:
    """
    Find a Hamiltonian cycle in the given graph represented as a list of linked lists.

    :param graph_data: List of Linked_List objects representing the adjacency list of the graph.
    :return: None (prints the Hamiltonian cycle if found, otherwise indicates failure).
    """
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
            # Check if there's an edge back to the start./
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
        header("HAMILTONIAN CYCLE FOUND")
        print("Hamiltonian cycle found:")
        line("-")
        print_text_multiline(path, path=True)
        footer()
    else:
        header("HAMILTONIAN CYCLE NOT FOUND","\\!/")
