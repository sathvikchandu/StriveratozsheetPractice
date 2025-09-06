"""
What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

Examples
Input Format: N = 5, array[] = {5,4,3,2,1}
Result: 10
Explanation: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.
"""


from typing import List
import math

def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1 # starting index of right half of arr

    cnt = 0     # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Modification 2
            right += 1

    # if elements on the left half are still left
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt   # Modification 3

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    n = len(a)
    # Count the number of pairs:
    return mergeSort(a, 0, n - 1)

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print("The number of inversions are:", cnt)


