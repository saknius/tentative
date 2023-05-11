# agonostic binary search
# this is very basic

def binary_search_first_and_last_occurance(nums):
    n = len(nums)
    start = 0
    end = n - 1
    if n==1:
        return nums[0]
    while start <= end :
        mid = start + (end-start)//2
        prev = (mid + n - 1)%n
        next = (mid + 1)%n
        if (nums[mid] < nums[prev] and nums[mid] < nums[next]):
            return nums[mid]
        elif nums[end] < nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == '__main__':
    import time
    nums = [120, 100, 220, 120, 100, 120]
    nums.sort()
    print(nums)
    intial_time = time.time()
    print(binary_search_first_and_last_occurance(nums))
    print((time.time() - intial_time)*1000)


