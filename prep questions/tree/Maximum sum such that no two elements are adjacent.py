# Function to find the maximum sum
def rec(nums, idx):
	if idx >= len(nums):
		return 0
	return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))

def findMaxSum(arr, N):
	return rec(arr, 0)

# Driver Code
if __name__ == "__main__":
	# Creating the array
	arr = [5, 5, 10, 100, 10, 5]
	N = len(arr)

	# Function call
	print(findMaxSum(arr, N))

# basic approach


# logic samaj nhi aaya abhi toh

def findMaxSum(nums, N):
	dp = [-1] * (N + 1)

	def rec(idx, dp):
		if idx >= len(nums):
			return 0
		if dp[idx] != -1:
			return dp[idx]
		dp[idx] = max(rec(idx + 1, dp), nums[idx] + rec(idx + 2, dp))
		return dp[idx]

	return rec(0, dp)


# Driver Code
arr = [5, 5, 10, 100, 10, 5]
N = len(arr)

print(findMaxSum(arr, N))

# ye uska hi memoized version hai i guess

