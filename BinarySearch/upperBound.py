"""
The upper bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than a given key i.e. x.

Input : n= 4, nums = [1,2,2,3], x = 2

Output:3
"""

nums=[3,5,6,8,15,19]
x=9
n=len(nums)
low=0
high=n-1
ans=n

while low<=high:
    
    mid=(low+high)//2
    
    if nums[mid]>x:
        
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)

