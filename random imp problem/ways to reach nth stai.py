"""
same as file name
"""

def count_ways_to_reach_stair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# Example usage:
n = 100000
for i in range(2, n):  
    num_ways = count_ways_to_reach_stair(i)
    print("Number of ways to reach the", i, "th stair:", num_ways)
