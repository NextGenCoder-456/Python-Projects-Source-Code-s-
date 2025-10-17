import time
import math

def measure(func, inputs, repeats=3):
    """Measures average runtime of func on each input in inputs."""
    results = []
    for n in inputs:
        times = []
        for _ in range(repeats):
            start = time.perf_counter()
            func(n)
            end = time.perf_counter()
            times.append(end - start)
        avg = sum(times) / len(times)
        results.append((n, avg))
    return results

# Example functions to test
def linear(n):
    s = 0
    for i in range(n):
        s += i
    return s

def quadratic(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += 1
    return s

def run_demo():
    sizes = [100, 300, 700, 1300]  # adjust for your machine
    print("Testing linear:")
    for n, t in measure(linear, sizes):
        print(f"n={n:<5} time={t:.6f}s")
    print("\nTesting quadratic:")
    for n, t in measure(quadratic, sizes):
        print(f"n={n:<5} time={t:.6f}s")

if __name__ == "__main__":
    run_demo()
