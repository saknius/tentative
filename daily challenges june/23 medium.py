class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxLen = 0
        dp = [{} for _ in range(len(nums))]

        for i in range(len(nums)):
            curr = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    curr[diff] = dp[j][diff] + 1
                else:
                    curr[diff] = 2
                maxLen = max(maxLen, curr[diff])
            dp[i] = curr

        return maxLen
