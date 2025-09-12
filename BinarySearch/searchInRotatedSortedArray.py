"""
Problem Statement
You are given a rotated sorted array arr of distinct integers and an integer k. The array was originally sorted in ascending order but has been rotated at some pivot unknown to you beforehand. Your task is to find the index of the target integer k in the array. If the target does not exist in the array, return -1.

Constraints:

The array contains distinct integers.
The array is rotated at some pivot (e.g., [4, 5, 6, 7, 0, 1, 2] is a rotated version of [0, 1, 2, 4, 5, 6, 7]).
The solution must run in O(log n) time complexity.


"""

from typing import List


class Solution:
    def search(self, arr: List[int], k: int) -> int:
        """
        Searches for the target value 'k' in a rotated sorted array 'arr'.
        
        Args:
        arr (List[int]): The rotated sorted array of distinct integers.
        k (int): The target value to search for.

        Returns:
        int: The index of the target value 'k' if found, otherwise -1.
        """
        n = len(arr)  # Length of the array

        # Initialize pointers for binary search
        low = 0
        high = n - 1

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle index

            # Check if the middle element is the target
            if arr[mid] == k:
                return mid
            
            # Check if the left half is sorted
            elif arr[low] <= arr[mid]:
                # If the target lies within the sorted left half
                if arr[low] <= k <= arr[mid]:
                    high = mid - 1  # Narrow the search to the left half
                else:
                    low = mid + 1  # Narrow the search to the right half
            else:
                # If the target lies within the sorted right half
                if arr[mid] <= k <= arr[high]:
                    low = mid + 1  # Narrow the search to the right half
                else:
                    high = mid - 1  # Narrow the search to the left half

        # If the target is not found, return -1
        return -1