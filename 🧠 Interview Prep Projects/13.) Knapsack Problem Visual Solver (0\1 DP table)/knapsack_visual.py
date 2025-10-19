# knapsack_visual.py
# Builds DP table for 0/1 knapsack and prints the table for visualization.

def knapsack(values, weights, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(0, W+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    return dp

def print_table(dp, values, weights):
    n = len(values)
    print("DP table (rows: items 0..n, cols: capacity 0..W):")
    for i, row in enumerate(dp):
        label = "0" if i==0 else f"item{i} (v{values[i-1]} w{weights[i-1]})"
        print(f"{label:20} | " + " ".join(f"{x:3}" for x in row))

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    dp = knapsack(values, weights, W)
    print_table(dp, values, weights)
    print("Max value:", dp[len(values)][W])
