#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

data=[2,2,1,1,1,2,2]

data.sort()
print(data[len(data)//2])
