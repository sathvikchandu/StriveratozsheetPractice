nums=[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]


nums.sort()
n=len(nums)
s=set()

for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    j=i+1
    k=n-1
    while j<=k:
        total=nums[i]+nums[j]+nums[k]
        if total<0:
            j+=1
        elif total>0:
            k-=1
        else:
            s.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1

            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1

s=list(s)
s= [list(i) for i in s]
print(s)