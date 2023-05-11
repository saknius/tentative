# agonostic binary search
# this is very basic

def binary_search_first_and_last_occurance(nums, target):
    n = len(nums)
    start,  end = 0, n-1
    first, last = -1, 1
    while start <= end:
        mid = start + (end-start)//2
        if target == nums[mid]:
            first = mid
            end = mid - 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end-start)//2
        if target == nums[mid]:
            last = mid
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if last == -1 and first == -1:
        return 0
    res = last - first + 1
    return res


    return

if __name__ == '__main__':
    import time
    nums = [120, 100, 220, 120, 100, 120]
    target = 120
    nums.sort()
    print(nums)
    intial_time = time.time()
    print(binary_search_first_and_last_occurance(nums, target))
    print((time.time() - intial_time)*1000)


