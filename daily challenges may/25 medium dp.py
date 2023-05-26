def probabilityOfPoints(k, maxPts, n):
    dp = [[0] * (n+1) for _ in range(k+1)]
    dp[0][0] = 1

    for i in range(1, k+1):
        for j in range(n+1):
            for x in range(1, min(j, maxPts)+1):
                dp[i][j] += dp[i-1][j-x] / maxPts

    probability = sum(dp[k][:n+1])
    return probability