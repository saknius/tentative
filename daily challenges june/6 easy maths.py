"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
"""

def canMakeArithmeticProgression(self, arr):
    arr.sort()
    n = len(arr)
    if n<=2:
        return True
    else:
        m = arr[1]-arr[0]
        for i in range(2,n):
            if arr[i]-arr[i-1]!=m:
                return False
        return True
    return True