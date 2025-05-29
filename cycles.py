from lists import Linked_List
from copy import deepcopy


def find_euler_cycle(graph_data: list[Linked_List]) -> None:
    """
    Find an Euler cycle in the given graph represented as a list of linked lists.
    :param graph_data: List of Linked_List objects representing the adjacency list of the graph.
    :return: None (prints the Euler cycle if found, otherwise indicates failure).
    
    """
    n = len(graph_data)
    adj = {i+1: [] for i in range(n)}
    for idx, linked_list in enumerate(graph_data, start=1):
        current = linked_list.head
        while current:
            if current.data != idx:  # avoid self-loops
                adj[idx].append(current.data)
            current = current.next

    # Check if all degrees are even
    for v in adj:
        if len(adj[v]) % 2 != 0:
            print("No Euler cycle: vertex", v, "has odd degree.")
            return

    # Hierholzer's algorithm
    stack = [1]
    path = []
    local_adj = deepcopy(adj)

    while stack:
        v = stack[-1]
        if local_adj[v]:
            u = local_adj[v].pop()
            local_adj[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())

    if len(path) == sum(len(neigh) for neigh in adj.values()) // 2 + 1:
        print("Euler cycle found:")
        print(" -> ".join(map(str, path[::-1])))
    else:
        print("Euler cycle not found (graph may be disconnected).")


def find_hamilton_cycle(graph_data: list[Linked_List]) -> None:
    """
    Find a Hamiltonian cycle in the given graph represented as a list of linked lists.
    :param graph_data: List of Linked_List objects representing the adjacency list of the graph.
    :return: None (prints the Hamiltonian cycle if found, otherwise indicates failure).
    """
    n = len(graph_data)
    path = [1]  # Start from vertex 1 (assuming 1-based indexing)

    def neighbors(v):
        """Yield neighbors of vertex v (1-based index) from the Linked_List."""
        current = graph_data[v-1].head
        while current:
            if current.data != v:  # avoid self-loops
                yield current.data
            current = current.next

    def backtrack(v, visited):
        if len(path) == n:
            # Check if there's an edge back to the start
            if path[0] in list(neighbors(v)):
                path.append(path[0])
                return True
            return False
        for u in neighbors(v):
            if u not in visited:
                visited.add(u)
                path.append(u)
                if backtrack(u, visited):
                    return True
                path.pop()
                visited.remove(u)
        return False

    visited = set([1])
    if backtrack(1, visited):
        print("Hamiltonian cycle found:")
        print(" -> ".join(map(str, path)))
    else:
        print("Hamiltonian cycle not found.")