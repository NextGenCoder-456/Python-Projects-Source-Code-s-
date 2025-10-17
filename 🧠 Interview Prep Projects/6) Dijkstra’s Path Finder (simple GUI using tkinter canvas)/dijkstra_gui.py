import tkinter as tk
import heapq
import math

# simple graph with positions for drawing
graph = {
    'A': {'B':5, 'C':2},
    'B': {'A':5, 'D':2, 'E':3},
    'C': {'A':2, 'F':7},
    'D': {'B':2, 'E':1},
    'E': {'B':3, 'D':1, 'F':5},
    'F': {'C':7, 'E':5}
}
pos = {'A':(50,50),'B':(200,50),'C':(50,200),'D':(200,200),'E':(350,150),'F':(150,350)}

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
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, prev

def get_path(prev, target):
    path = []
    cur = target
    while cur in prev:
        path.append(cur)
        cur = prev[cur]
    path.append(cur)
    return list(reversed(path))

# GUI
root = tk.Tk()
root.title("Dijkstra Visual")
canvas = tk.Canvas(root, width=500, height=450, bg='white')
canvas.pack()

# draw edges
for u, nbrs in graph.items():
    x1,y1 = pos[u]
    for v,w in nbrs.items():
        x2,y2 = pos[v]
        canvas.create_line(x1, y1, x2, y2, fill='gray')
        mx,my = (x1+x2)//2, (y1+y2)//2
        canvas.create_text(mx, my, text=str(w), fill='blue')

# draw nodes
node_items = {}
for n,(x,y) in pos.items():
    node_items[n] = canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightgray')
    canvas.create_text(x, y, text=n)

def run(start, target):
    dist, prev = dijkstra(start)
    path = get_path(prev, target)
    # reset
    for n in node_items:
        canvas.itemconfig(node_items[n], fill='lightgray')
    # highlight path
    for n in path:
        canvas.itemconfig(node_items[n], fill='orange')
    canvas.update()
    print("Shortest distance:", dist[target], "Path:", path)

# simple controls
start_var = tk.StringVar(value='A')
target_var = tk.StringVar(value='F')
tk.Entry(root, textvariable=start_var).pack(side='left')
tk.Entry(root, textvariable=target_var).pack(side='left')
tk.Button(root, text='Find Path', command=lambda: run(start_var.get().strip(), target_var.get().strip())).pack(side='left')

root.mainloop()
