
nums=[4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target=9
n=len(nums)

ans=[]

nums.sort()

for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue

        k=j+1

        l=n-1

        while k<l:
            temp=nums[i]+nums[j]+nums[k]+nums[l]
            if temp==target:
                ans.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while l>k and nums[l]==nums[l+1]:
                    l-=1
            elif temp<target:
                k+=1
            else:
                l-=1
print(ans)


