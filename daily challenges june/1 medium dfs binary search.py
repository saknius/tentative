"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

"""
examples:

"""
from collections import deque

# class Solution:
#     def __init__(self, grid):
#         self.grid = grid
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] ==1 or grid[n-1][n-1]==1:
        return -1
    queue = deque([(0,0,1)])

    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True

    directions = [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    while queue:
        x, y, dist = queue.popleft()
        if x == n-1 and y == n-1:
            return dist
        for dx, dy in directions:
            nx , ny = x+dx, y+dy
            if 0<= nx< n  and 0<= ny< n and grid[nx][ny] == 0  and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny, dist+1))
    return -1
# Solution([[1,0,0],[1,1,0],[1,1,0]])    
shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
"""
gpt solution 
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    # Check if the starting or target cell is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Initialize the queue with starting cell and distance
    queue = deque([(0, 0, 1)])
    
    # Create a visited matrix and mark the starting cell as visited
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    # Define eight possible directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    # Perform BFS
    while queue:
        x, y, dist = queue.popleft()
        
        # Check if the target cell is reached
        if x == n - 1 and y == n - 1:
            return dist
        
        # Explore all eight directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the adjacent cell is within bounds and has a clear path
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1  # No clear path found

# Example usage:
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))  # Output: 4
"""

"""
wrong in example [[1,0,0],[1,1,0],[1,1,0]]

"""