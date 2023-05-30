# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# Accepted
# 1.5M
# Submissions
# 1.9M
# Acceptance Rate
# 75.2%
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Discussion (25)
# Similar Questions
# Related Topics
# Copyright ©️ 2023 LeetCode All rights reserved

class Solution:
    def subset(nums):
        res = []
        subset = []
        def dfs(i):
            # decision to include nums[i]
            if i>=len(nums)-1:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)


        dfs(0)
        return res
    # makes a littile bit of sense


def find_subsets(nums):
    subsets = []
    backtrack(nums, [], subsets, 0)
    return subsets

def backtrack(nums, current_subset, subsets, start_index):
    subsets.append(list(current_subset))

    for i in range(start_index, len(nums)):
        current_subset.append(nums[i])
        backtrack(nums, current_subset, subsets, i + 1)
        current_subset.pop()

# Example usage
nums = [1, 2, 3]
subsets = find_subsets(nums)
print(subsets)
