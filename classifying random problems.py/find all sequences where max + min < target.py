

def lcs_variation(nums):
    length = len(nums)
    matrix = [[-1]*(length+1) for i in range(length+1)]
    for row_itr in range(0, length+1):
        for column_itr in range(0,length+1):
            if row_itr==0 or column_itr==0:
                matrix[row_itr][column_itr]=0

    return 1

def common_lcs(str1, str2):
    n = len(str1)
    m = len(str2)
    matrix = [[-1]*(m+1) for i in range(n+1)]
    for row_itr in range(0, n+1):
        for column_itr in range(0,m+1):
            if row_itr==0 or column_itr==0:
                matrix[row_itr][column_itr]=0
    for row_itr in range(1, n+1):
        for column_itr in range(1,m+1):
            if str1[row_itr-1] == str2[column_itr-1]:
                matrix[row_itr][column_itr] = 1 + matrix[row_itr-1][column_itr-1]
            else:
                matrix[row_itr][column_itr] = max(matrix[row_itr-1][column_itr], matrix[row_itr][column_itr-1])
    return matrix[n][m]



def num_seq(nums, target):
    nums_length = len(nums)
    # probably a general formula
    # looks to difficult in first see
    # could be some stack logic
    # because even size can be ant yhin no so eve more confusing
    # nums = [2,3,3,4,6,7], target = 12
    # this test case has only six element and out of that 64 sub sequences only two has sum more then 12
    total_non_empty_subsequences = 2**(nums_length) - 1
    # two pointer maybe ....
    # left_pointer, right_pointer = 0, 0
    # total_sequence = 0
    # for left_pointer in range(nums_length):
    #     for right_pointer in range(left_pointer,nums_length):
    #         current_sequence = nums[left_pointer,right_pointer+1]
    #         min_nums = min(nums)
    #         max_nums = max(nums)
    #         if min_nums + max_nums <= target:
    #             total_sequence += 1
    #             right_pointer+=1
    # approch two pointer nhi lcs wala hi h sayad
    total_greater_sum = lcs_variation(nums)
    total_sequence = total_non_empty_subsequences - total_greater_sum
    return total_sequence


if __name__ == '__main__':
    nums = [3,5,6,7]
    target = 9
    str1 = 'dcheckll'
    str2 = 'eckl'
    print(common_lcs(str1, str2))
    print(num_seq(nums, target))



# int LCS(string X, string Y, int n, int m) {
# 	int dp[n + 1][m + 1]; // DP - matrix

# 	// initialize 1st row and of dp matrix with 0 according to the base condition of recursion // base case of recursion --> for initialization of dp - matrix
# 	for (int i = 0; i <= n; i++)
# 		for (int j = 0; j <= m; j++)
# 			if (i == 0 || j == 0)
# 				dp[i][j] = 0;
# // choise diagram is used to fill rest of the matrix
# 	for (int i = 1; i <= n; i++)
# 		for (int j = 1; j <= m; j++)
# 			if (X[i - 1] == Y[j - 1]) // when last character is same
# 				dp[i][j] = 1 + dp[i - 1][j - 1];
# 			else // when last character is not same -> pick max
# 				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);

# 	return dp[n][m]; // last row and last column element will give the length of the LCS;
# }
