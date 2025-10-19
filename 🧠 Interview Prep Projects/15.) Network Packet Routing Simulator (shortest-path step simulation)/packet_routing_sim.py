# packet_routing_sim.py
# Simulates sending a packet from source to destination along shortest path (Dijkstra).
import heapq
import time

graph = {
    'A': {'B':2, 'C':5},
    'B': {'A':2, 'C':1, 'D':4},
    'C': {'A':5, 'B':1, 'D':1, 'E':7},
    'D': {'B':4, 'C':1, 'E':3},
    'E': {'C':7, 'D':3}
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    prev = {}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d,u = heapq.heappop(heap)
        if d>dist[u]: continue
        for v,w in graph[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v]=nd
                prev[v]=u
                heapq.heappush(heap, (nd, v))
    return dist, prev

def reconstruct(prev, src, dst):
    path = []
    cur = dst
    while cur != src:
        path.append(cur)
        cur = prev.get(cur)
        if cur is None:
            return []
    path.append(src)
    return list(reversed(path))

def simulate_packet(src, dst, step_delay=1.0):
    dist, prev = dijkstra(src)
    path = reconstruct(prev, src, dst)
    if not path:
        print("No path found")
        return
    print("Routing path:", " -> ".join(path))
    for node in path:
        print(f"Packet at {node}")
        time.sleep(step_delay)
    print("Packet arrived at destination.")

if __name__ == "__main__":
    simulate_packet("A", "E", step_delay=0.8)
