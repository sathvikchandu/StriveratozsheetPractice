# can include negatives

nums=[5,4,-1,7,8]

max_sum=0

i=0
temp_sum=0
while i<len(nums):
    temp_sum+=nums[i]
    if temp_sum<0:
        temp_sum=0
    max_sum=max(max_sum,temp_sum)
    i+=1

if max_sum==0:
    print(max(nums))
else:
    print(max_sum)


"""
Ideal solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, sol = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            sol = max(sol, cur_sum)
        return sol

"""
