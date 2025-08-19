"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        idx = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        # Step 2: If not found, reverse whole list
        if idx == -1:
            nums.reverse()
            return

        # Step 3: Find the next larger element to swap
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break   # important!!

        # Step 4: Reverse the suffix
        nums[idx + 1:] = reversed(nums[idx + 1:])


