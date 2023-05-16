# agonostic binary search
# this is very basic


def next_alphabetical_element(nums, target):
    n = len(nums)
    if target>=nums[n-1]:
        return nums[0]
    l = 0
    r = len(nums) - 1
    ans = -1
    while l<=r:
        mid = int(l+r)//2
        if nums[mid] > target:
            r = mid -1
            ans = mid
        else:
            l = mid + 1
    if (nums[ans]<target):
        return nums[0]
    return nums[ans]


if __name__ == '__main__':
    import time
    nums = ['A', 'r', 'z']
    target = 'z'
    intial_time = time.time()
    print(next_alphabetical_element(nums, target))
    print((time.time() - intial_time)*1000)


