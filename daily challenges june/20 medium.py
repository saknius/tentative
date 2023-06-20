"""
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
Example 2:

Input: nums = [100000], k = 0
Output: [100000]
Explanation:
- The sum of the subarray centered at index 0 with radius 0 is: 100000.
  avg[0] = 100000 / 1 = 100000.
Example 3:

Input: nums = [8], k = 100000
Output: [-1]
Explanation: 
- avg[0] is -1 because there are less than k elements before and after index 0.
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105
Accepted
49.5K
Submissions
105.3K
Acceptance Rate
47.0%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (44)
Similar Questions
Related Topics
Copyright ©️ 2023 LeetCode All rights reserved
"""

# class List(list):
#     def __init__(self, *args):
#         super().__init__(args)

#     def add_element(self, element):
#         self.append(element)

#     def remove_element(self, element):
#         if element in self:
#             self.remove(element)3
#         else:
#             print(f"{element} not found in the list.")

#     def display(self):
#         print(self)

# class Solution:
def getAverages( nums: list[int], k: int) -> list[int]:
        
    n = len(nums)
    windowSize = 2 * k + 1
    ans = [-1] * n

    if n < windowSize:
        return ans

    prefixSum = [0] * (n + 1)
    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + nums[i]

    for i in range(k, n - k):
        ans[i] = (prefixSum[i + k + 1] - prefixSum[i - k]) // windowSize

    return ans

getAverages([8], 100000)

