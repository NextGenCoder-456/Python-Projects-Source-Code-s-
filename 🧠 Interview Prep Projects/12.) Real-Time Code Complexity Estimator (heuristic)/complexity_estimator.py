# complexity_estimator.py
# Heuristic empirical estimator: times function on growing n and compares growth to n, n*logn, n^2.
import time
import math

def measure_time(func, n, repeats=3):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

def estimate_growth(sizes, times):
    # Compare ratios with reference growth functions
    def score_with(f_vals):
        # compute how well times match f_vals via linear regression slope error (simple)
        ratios = [t / fv if fv>0 else float('inf') for t, fv in zip(times, f_vals)]
        mean = sum(ratios) / len(ratios)
        var = sum((r-mean)**2 for r in ratios) / len(ratios)
        return var  # lower variance => better fit
    f_n = [n for n in sizes]
    f_nlogn = [n * math.log(n+1) for n in sizes]
    f_n2 = [n*n for n in sizes]
    f_log = [math.log(n+1) for n in sizes]
    candidates = {
        "O(n)": score_with(f_n),
        "O(n log n)": score_with(f_nlogn),
        "O(n^2)": score_with(f_n2),
        "O(log n)": score_with(f_log),
        "O(1)": score_with([1]*len(sizes))
    }
    return min(candidates.items(), key=lambda x: x[1])[0]

# Example test functions
def linear(n):
    s=0
    for i in range(n):
        s+=i
    return s

def quadratic(n):
    s=0
    for i in range(n):
        for j in range(n):
            s+=1
    return s

if __name__ == "__main__":
    funcs = [("linear", linear), ("quadratic", quadratic)]
    sizes = [200, 500, 1000]  # adjust to machine
    for name, f in funcs:
        times = [measure_time(f, n) for n in sizes]
        guess = estimate_growth(sizes, times)
        print(f"{name}: times={['{:.4f}'.format(t) for t in times]} => guessed {guess}")
