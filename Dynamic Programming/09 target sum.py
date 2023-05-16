def CountSubsetsWithSum(nums, sum):
    n = len(nums)
    t = [[False]*(n+1) for i in range(sum+1)]
    t[0][0] = 1
    k = 1
    for i in range(n+1):
        for j in range(sum+1):
            if i==0 and j>0:
                t[i][j] = 0
            if j==0 and i>0:
                if nums[i-1] == 0:
                    t[i][j] = 2**k
                    k+=1
                else:
                    t[i][j] = t[i-1][j]
    for i in range(1,n+1):
        for j in range(1, sum+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j - nums[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]

if __name__ == "__main__":
    print('1')
