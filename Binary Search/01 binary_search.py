# peak element


def binary_search_target_sum(nums, target):
    n = len(nums)
    start,  end = 0, n-1
    while start <= end:
        mid = start + (end-start)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    import time
    nums = [220, 100, 100, 120, 100, 120]
    target = 220
    nums.sort()
    intial_time = time.time()
    print(binary_search_target_sum(nums, target))
    print(time.time() - intial_time)


