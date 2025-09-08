"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

nums=[1,3,5,6]
target=5

n=len(nums)
low=0
high=n-1

n = len(nums)
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(mid)  # Target found, print the index
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    # If the loop exits, `low` is the correct insert position
    print(low)
    