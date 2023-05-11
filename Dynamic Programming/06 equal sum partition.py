def CountSubsets(arr, n, target_sum):
    t = [ [False]*(target_sum+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(target_sum+1):
            if i==0:
                # when array is empty there is no means of sum of element so return count of subset as 0
                t[i][j] = 0
            if j==0:
                # when sum is zero thr  there is always chance of empty subset so
                t[i][j] = 1
    for i in range(1,n+1):
        for j in range(1, target_sum+1):
            # when element in the list is less then target sum
            if arr[i-1] <= j:
                # either exclude or include or add both of them to the final count
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                # exclude  when e in the list is greaterlement then the sum
                t[i][j] = t[i-1][j]
    return t[n][target_sum]

if __name__ == '__main__':
    arr = [1,2,4,1,2,3,1]
    n = len(arr)
    target_sum = 12
    print(CountSubsets(arr,n,target_sum))


