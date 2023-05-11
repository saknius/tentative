
def isSubsetPossible(arr, n, target_sum):
    # t = [ [False]*(target_sum+1) for i in range(n+1)]

    for i in range(0, n+1):
        for j in range(0, target_sum+1):
            if i==0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
    for i in range(1,n+1):
        for j in range(i, target_sum+1):
            if arr[i-1]<=j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target_sum]

if __name__ == '__main__':
    arr = [ 1,3,4,5,6,6]
    n = len(arr)
    target_sum = 99
    p = isSubsetPossible(arr, n, target_sum)
    print(p)

