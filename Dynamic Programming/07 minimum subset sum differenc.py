import sys

def isSubsetPoss(arr, n , sum):
    t =[[False]*n for i in range(sum)]
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1]<=j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    v = []
    for j in range(sum+1):
        if t[n][j] == True:
            v.append(j)

    return v

def minimum_diff(arr, n):
    range = 0
    for i in range(0, n):
        range += arr[i]
    v = isSubsetPoss(arr, n, range)
    mn = sys.maxint
    for i in range(n)
    return

if __name__ == 'main':
    arr = []
    n = len(arr)
    print(minimum_diff(arr, n))
