"""
Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.


"""

"""
time constraints
m == mat.length 
n == mat[i].length 
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105
"""

"""
views:
too much generalized problem

"""

"""
gpts solution
def maxVisitedCells(mat):
    m, n = len(mat), len(mat[0])
    dp = [[1] * n for _ in range(m)]

    for i in range(m-2, -1, -1):
        if mat[i][n-1] > mat[i+1][n-1]:
            dp[i][n-1] = 1 + dp[i+1][n-1]

    for j in range(n-2, -1, -1):
        if mat[m-1][j] > mat[m-1][j+1]:
            dp[m-1][j] = 1 + dp[m-1][j+1]

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            if mat[i][j] < mat[i+1][j]:
                dp[i][j] = max(dp[i][j], 1 + dp[i+1][j])
            if mat[i][j] < mat[i][j+1]:
                dp[i][j] = max(dp[i][j], 1 + dp[i][j+1])

    return dp[0][0]
i don't think this will work as it assumes we are starting from point 
"""


# class Solution:
def maxIncreasingCells(self, mat) -> int:
    m, n = len(mat), len(mat[0])
    dp = [[1]*n for _ in range(m)]

    for i in range(m-2, -1, -1):
        if mat[i][n-1] > mat[i+1][n-1]:
            dp[i][n-1] = 1 + dp[i+1][n-1]
    for j in range(n-2, -1, -1):
        if mat[m-1][j] > mat[m-1][j+1]:
            dp[m-1][j] = 1 + dp[m-1][j+1]
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            if mat[i][j] < mat[i+1][j]:
                dp[i][j] = max(dp[i][j], 1+dp[i+1][j])
            if mat[i][j] < mat[i][j+1]:
                dp[i][j] = max(dp[i][j], 1+dp[i][j+1])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(dp[i][j],ans)
    return ans


def maxIncreasingCells2(self, mat) -> int:
    m, n = len(mat), len(mat[0])
    r, c = [0] * m, [0] * n
    vmap = {}
    from sortedcontainers import SortedSet
    s = SortedSet()
    for i in range(0, m):
        for j in range(0, n):
            if not -mat[i][j] in vmap:
                vmap[-mat[i][j]] = []
            vmap[-mat[i][j]].append([i, j])
            s.add(-mat[i][j])
    temp = [[0] * n for _ in range(m)]
    for x in s:
        for v in vmap.get(x):
            temp[v[0]][v[1]] = max(r[v[0]], c[v[1]]) + 1
        for v in vmap.get(x):
            r[v[0]] = max(r[v[0]], temp[v[0]][v[1]])
            c[v[1]] = max(c[v[1]], temp[v[0]][v[1]])
    return max(max(r), max(c))
maxIncreasingCells('s')
    

"""
Let m and n be the number of rows and columns of the matrix.
Create 2 arrays r and c whose lengths are m and n.
Initialize them to all 0s. 
They are the maximum path length of each row or column.
Sort all the values in the matrix in non increasing order,
for each value v, save all the positions (x, y) of that value in a list (reverse indexed).
Loop all the values from largest to smallest,
for each v, all the occurrence positions (x, y),
save temp[x][y] = max(r[x], c[y]) + 1, 
this is the longest path starting from that value.
Update r[x] = max(r[x], temp[x][y]) and c[y] = max(c[y],
temp[x][y]) for all the above (x, y)s. 
This is to update the longest path for each row and column.
Also note this step should be done after step 3 is fully complete.
The maximum value in arrays r and c is the final answer.
longest path in each row and column toh asamjb gaya woh sorted arraye kyu lia woh nhi samjha

"""   

"""
looking into the solution
 class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        r, c = [0] * m, [0] * n
        vmap = {}
        from sortedcontainers import SortedSet
        s = SortedSet()
        for i in range(0, m):
            for j in range(0, n):
                if not -mat[i][j] in vmap:
                    vmap[-mat[i][j]] = []
                vmap[-mat[i][j]].append([i, j])
                s.add(-mat[i][j])
        temp = [[0] * n for _ in range(m)]
        for x in s:
            for v in vmap.get(x):
                temp[v[0]][v[1]] = max(r[v[0]], c[v[1]]) + 1
            for v in vmap.get(x):
                r[v[0]] = max(r[v[0]], temp[v[0]][v[1]])
                c[v[1]] = max(c[v[1]], temp[v[0]][v[1]])
        return max(max(r), max(c))
kuch logic samajh nhi arra

"""

"""
how is this a dp problem??
"""