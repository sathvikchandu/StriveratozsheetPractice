"""
Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

LOGIC

if I want to find the number of subarray with xor k, I should first find an x when xored with remaining subarray gives me k

In this approach, we are going to use the concept of the prefix XOR to solve this problem. Here, the prefix XOR of a subarray ending at index i, simply means the XOR of all the elements of that subarray.

Observation: Assume, the prefix XOR of a subarray ending at index i is xr. In that subarray, we will search for another subarray ending at index i, whose XOR is equal to k. Here, we need to observe that if there exists another subarray ending at index i, with XOR k, then the prefix XOR of the rest of the subarray will be xr^k. The below image will clarify the concept:

Now, for a subarray ending at index i with the prefix XOR xr, if we remove the part with the prefix XOR xr^k, we will be left with the part whose XOR is equal to k. And that is what we want.
"""

nums= [4, 2, 2, 6, 4]
k = 6

d={}
res=0
xor=0
d[0]=1
for i in nums:
    xor=xor^i
    temp=xor^k
    if temp in d:
        res+=d[temp]
        d[temp]+=1
    else:
        d[temp]=1
print(res)