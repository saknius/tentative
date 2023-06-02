"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
 xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb.
When a bomb is detonated,
it will detonate all bombs that lie in its range.
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, 
return the maximum number of bombs that can be detonated 
if you are allowed to detonate only one bomb.
"""

"""
gpt
     max_detonations = 0
    
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            detonations = 1  # Initialize with 1 for the current bomb
            
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                    
                    if distance <= r1:
                        detonations += 1  # Increment detonations if bomb is within range
            
            max_detonations = max(max_detonations, detonations)
        
        return max_detonations
"""
"""
like that black and white chinese game one move will have a butterfly effect and i have to maximize the effect
how do i find cocentric cricles 
"""

# class Solution:
def maximumDetonation(bombs) -> int:
    max_detonations = 0
    for i in range(len(bombs)):
        x1, y1, r1 = bombs[i]
        detonations = 1
        for j in range(len(bombs)):
            if i!=j:
                x2, y2, r2 = bombs[j]
                distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
                if distance <= (r1 + r2) and distance >= abs(r1 - r2):
                    detonations+=1
        max_detonations = max(max_detonations, detonations)
    print(max_detonations)
    return max_detonations
# maximumDetonation(([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])
maximumDetonation([[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]])

"""
both time complexity and logix are doubtable here
class Solution:
    def maximumDetonation(self, bombs):
        n, max_bombs, graph = len(bombs), 0, defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i] += [j]

        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs
    
why are they applying dfs on such a simple problem

"""
from collections import defaultdict
def maximumDetonation(bombs) -> int:
    n, max_bombs, graph = len(bombs), 0, defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
            if i!=j and r1>=distance:
                graph[i] +=[j]
    def dfs(node, visited):
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                dfs(child, visited)
    for i in range(n):
        visited = set([i])
        dfs(i, visited)
        max_bombs = max(max_bombs, len(visited))

    return max_bombs 
