"""
You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
"""

nums = [3,1,-2,-5,2,-4]
pos_idx,neg_idx=0,1
res_arr=[0]*len(nums)
for i in nums:
    if i>0:
        res_arr[pos_idx]=i
        pos_idx+=2
    else:
        res_arr[neg_idx]=i
        neg_idx+=2
print(res_arr)

