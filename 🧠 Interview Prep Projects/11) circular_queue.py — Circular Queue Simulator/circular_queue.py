# circular_queue.py
# Simple Circular Queue implementation with fixed capacity and basic CLI demo.

class CircularQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_full(self):
        return self.size == self.cap

    def is_empty(self):
        return self.size == 0

    def enqueue(self, val):
        if self.is_full():
            raise Exception("Queue is full")
        self.arr[self.rear] = val
        self.rear = (self.rear + 1) % self.cap
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def __repr__(self):
        return f"Queue({self.arr}, front={self.front}, rear={self.rear}, size={self.size})"

# Demo CLI
if __name__ == "__main__":
    q = CircularQueue(5)
    print("Circular Queue Simulator (capacity=5)")
    while True:
        cmd = input("Command (enq <x>/deq/peek/show/exit): ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "enq" and len(cmd) == 2:
            try:
                q.enqueue(cmd[1])
                print("Enqueued:", cmd[1])
            except Exception as e:
                print("Error:", e)
        elif cmd[0] == "deq":
            try:
                print("Dequeued:", q.dequeue())
            except Exception as e:
                print("Error:", e)
        elif cmd[0] == "peek":
            print("Front:", q.peek())
        elif cmd[0] == "show":
            print(q)
        elif cmd[0] == "exit":
            break
        else:
            print("Invalid command")
