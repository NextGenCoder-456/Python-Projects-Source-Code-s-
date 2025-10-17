import heapq

def push(heap, val):
    print(f"Pushing {val}")
    heapq.heappush(heap, val)
    print("Heap:", heap)

def pop(heap):
    val = heapq.heappop(heap)
    print(f"Popped {val}")
    print("Heap:", heap)
    return val

if __name__ == "__main__":
    heap = []
    for v in [5, 3, 8, 1, 6]:
        push(heap, v)
    pop(heap)
    pop(heap)
    push(heap, 2)
