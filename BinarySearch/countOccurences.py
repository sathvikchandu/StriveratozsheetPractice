"""
You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.



Return the count of occurrences of target in the array.


"""

nums = [5,7,7,8,8,10]
target = 8

n=len(nums)
low=0
high=n-1

while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:

        temp=mid-1
        cnt=1
        while temp>=0 and nums[temp]==target:
            cnt+=1
            temp-=1
            
        right=mid+1
        while right<n and nums[right]==target:
            
            cnt+=1
            right+=1

        print(cnt)
        break
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
else:
    print(0)