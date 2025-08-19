

nums=[3,2,1]
idx=-1
n=len(nums)

for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
        idx=i
        break

if idx==-1:
    print(nums[::-1])

for i in range(n-1,idx,-1):
    if nums[i]>nums[idx]:
        nums[i],nums[idx]=nums[idx],nums[i]
nums1=nums[:idx+1]
nums2=nums[idx+1:]
nums2=nums2[::-1]

print(nums1+nums2)

