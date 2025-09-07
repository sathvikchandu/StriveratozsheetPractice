nums=[15, -2, 2, -8, 1, 7, 10, 23]
"""
You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.



Return the length of such a subarray. If no such subarray exists, return 0.

concept: prefix sum

"""
maxi=0
d={}
s=0

for i in range(len(nums)):
    s+=nums[i]

    if nums[i]==0:
        maxi=i+1
    
    else:
        if s in d:
            maxi=max(maxi,i-d[s])
        else:
            d[s]=i
print(maxi)