"""

Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero)
 needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the a
ssignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
"""

# class Solution:
#     def makeArrayIncreasing(self, arr1, arr2) -> int:
#         n = len(arr1)
#         m = len(arr2)
#         cnt=0
#         for i in range(n-1):
#             if arr1[i] < arr1[i+1]:
#                 continue
#             else:
#                 cnt+=1
#         for 
        # return -1
    


def min_operations(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    dp = [[float('inf')] * (n + 1) for _ in range(m)]
    dp[0] = [0] * (n + 1)
    for i in range(1, m):
        for j in range(n):
            if arr1[i] > arr1[i-1]:
                dp[i][j] = dp[i-1][j]
            
            if arr2[j] > arr1[i-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][0:j+1] + 1)
            
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
    min_ops = min(dp[-1])
    return min_ops if min_ops != float('inf') else -1

arr1 = [1,3,2,5,6,7,8,9,10,11,12,13]
arr2 = [3,1,4,1,2]
min_operations(arr1,arr2)