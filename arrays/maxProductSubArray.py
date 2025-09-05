nums=[-4,-3,-2]
max_sum=nums[0]
min_sum=nums[0]
res=nums[0]
n=len(nums)
if n==1:
    print(nums[0])
else:

    for i in range(1,n):
        #print("i is ",i)
        temp=max(nums[i],nums[i]*max_sum,nums[i]*min_sum)
        #print(temp)
        min_sum=min(nums[i],nums[i]*max_sum,nums[i]*min_sum)
        #print(min_sum)
        max_sum=temp
        #print(max_sum)
        res=max(res,max_sum)
        #print(res)
print(res)
