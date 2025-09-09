


"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

def searchRange(nums, target):
    def findFirst(nums, target):
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1  # Keep searching in the left half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def findLast(nums, target):
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1  # Keep searching in the right half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = findFirst(nums, target)
    last = findLast(nums, target)
    return [first, last]

# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]