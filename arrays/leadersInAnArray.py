
"""
Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.


"""
data=[4, 7, 1, 0]
data=data[::-1]

high=data[0]
start=data[1]

temp=[]
temp.append(high)
for i in range(1,len(data)):
    if high<data[i]:
        temp.append(data[i])
        high=data[i]

print(temp[::-1])
