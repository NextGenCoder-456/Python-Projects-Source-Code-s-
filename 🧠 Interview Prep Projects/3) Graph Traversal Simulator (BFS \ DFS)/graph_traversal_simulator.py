from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    order = []
    print("BFS steps:")
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        print(f"Visited {node}, enqueue neighbors: {graph.get(node, [])}")
        for nei in graph.get(node, []):
            if nei not in visited:
                q.append(nei)
    return order

def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []
    print("DFS steps (stack):")
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        print(f"Visited {node}, push neighbors: {graph.get(node, [])}")
        for nei in reversed(graph.get(node, [])):  # reverse to show natural order
            if nei not in visited:
                stack.append(nei)
    return order

if __name__ == "__main__":
    graph = {
        'A': ['B','C'],
        'B': ['D','E'],
        'C': ['F'],
        'D': [], 'E': ['F'], 'F': []
    }
    print("BFS order:", bfs(graph, 'A'))
    print("DFS order:", dfs(graph, 'A'))
