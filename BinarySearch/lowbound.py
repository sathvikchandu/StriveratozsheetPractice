"""
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x
"""


nums=[1,2,3,4,5]

x=4

n=len(nums)




low=0
high=n-1
ans=n

while low<=high:
    mid=(low+high)//2
    if nums[mid]>=x:
        ans=mid
        high=mid-1
    
    else:
        low=mid+1

print(ans)