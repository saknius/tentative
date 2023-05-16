# agonostic binary search
# this is very basic

def bs(nums, l, h, target):
    while l<=h:
        m = l+(h-l)//2
        if nums[m] == target:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            h = m -1
    return -1

def binary_search_for_rotated_sorted_array(nums, target):
    n = len(nums)
    if n == 1:
        if nums[0] == target:
            return 0
        return -1
    if nums[0] < nums[n-1]:
        return bs(nums, 0, n-1, target)
    pivot = -1
    l, h = 0, n-1
    while l<=h:
        m = l+(h-l)//2
        if (nums[m]<nums[(m+1)%n] and nums[m] < nums[(m-1+n)%n]):
            pivot = m
            break
        elif (nums[m]>=nums[0] and nums[m]>=nums[n-1]):
            l = (m+1)%n
        else:
            h = (m-1+n)%n
    if target >= nums[pivot] and target <= nums[n-1]:
        return bs(nums, pivot, n-1, target)
    return bs(nums, 0, pivot-1, target)



if __name__ == '__main__':
    nums = [120, 100, 220, 120, 100, 120]
    target = 100
    nums.sort()
    print(binary_search_for_rotated_sorted_array(nums, target))


