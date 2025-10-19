# toposort_visual.py
# Prints DFS steps and final topological order for a DAG.

def topo_dfs(graph):
    visited = {}
    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        if cycle:
            return
        visited[u] = 1  # visiting
        print(f"Visiting {u}")
        for v in graph.get(u, []):
            if visited.get(v, 0) == 0:
                dfs(v)
            elif visited.get(v) == 1:
                print("Cycle detected!", u, "->", v)
                cycle = True
                return
        visited[u] = 2
        order.append(u)
        print(f"Added {u} to order")

    for node in graph:
        if visited.get(node, 0) == 0:
            dfs(node)
    return list(reversed(order)), cycle

if __name__ == "__main__":
    g = {
        'A': ['C'],
        'B': ['C','D'],
        'C': ['E'],
        'D': ['F'],
        'E': [],
        'F': []
    }
    order, cyc = topo_dfs(g)
    if not cyc:
        print("Topological Order:", order)
