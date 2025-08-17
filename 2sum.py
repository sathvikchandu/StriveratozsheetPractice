nums=[3,2,4]

target=6
d={}
for i in range(len(nums)):
    
    diff=target-nums[i]
    if diff in d: 
        print([d[diff],i])
    else:
        d[nums[i]]=i

