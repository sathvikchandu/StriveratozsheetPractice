"""
This is my code which is wrong
nums=[1,1,1]
k=2

d={}

res=0

sub_sum=0
d[0]=1

for i in nums:
    sub_sum+=i
    if sub_sum-k in d:
        res+=d[sub_sum-k]
        d[sub_sum-k]+=1
    d[sub_sum]+=1
print(res)
"""

nums = [1, 1, 1]
k = 2

d = {}

res = 0

sub_sum = 0
d[0] = 1

for i in nums:
    sub_sum += i
    if sub_sum - k in d:
        res += d[sub_sum - k]
    d[sub_sum] = d.get(sub_sum, 0) + 1 
print(res)