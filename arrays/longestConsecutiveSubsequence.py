
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

nums=[100,4,200,1,3,2]

n=len(nums)

if n==0:
    print(0)
if n==1:
    print(1)

s=set(nums)


longest=1

for i in s:
    if i-1 not in s:
        cnt=1
        inc=i
        while inc+1 in s:
            cnt+=1
            inc+=1
        longest=max(longest,cnt)
print(longest)


