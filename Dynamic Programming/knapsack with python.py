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


