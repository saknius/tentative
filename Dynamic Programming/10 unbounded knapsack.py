def knapsack(wt, val, W, n):
    if n==0 or W==0:
        return 0
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt, val, W - wt[n-1],n-1), knapsack(wt, val, W, n-1))
    elif (wt[n-1]> W):
        return knapsack(wt, val, W, n-1)
    return -1

def knapsack_memo(wt, val, W, n):
    if n==0 or W==0:
        return 0
    if (t[n][W] != -1):
        return t[n][W]
    else:
        if wt[n-1] <= W:
            t[n][W] = max(val[n-1] + knapsack(wt, val, W - wt[n-1], n - 1), knapsack(wt, val, W, n-1))
        elif wt[n-1] > W:
            t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

def kanpsack_bottom_up_approach(wt, val, W, n):
    return

def unbounded_knapsack(wt, val, W, n):
    t = [[False]*(W+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                val1 = val[i-1] + t[i][j-wt[i-1]]
                val2 = t[i-1][j]
                t[i][j] = max(val1, val2)
            elif wt[i-1] > j:
                t[i][j] = t[i-1][j]
    return t[n][W]


if __name__ == '__main__':
    import time
    profit = [100, 100, 120, 100]
    weight = [10, 20, 30, 10]
    W = 50
    n = len(profit)
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    intial_time = time.time()
    print(knapsack(weight, profit, W, n))
    print(time.time() - intial_time)
    intial_time = time.time()
    print(knapsack_memo(weight, profit, W, n))
    print(time.time() - intial_time)
    intial_time = time.time()
    print(unbounded_knapsack(weight, profit, W, n))
    print(time.time() - intial_time)


