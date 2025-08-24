
#pascal triangle

numRows=5
flag=False
res=[]
res.append([1])
if numRows==1:
    flag=True

if flag==False:
    res.append([1,1])
if numRows==2:
    flag=True

if flag==False:
    result=2

    while result!=numRows:
        temp=[1]
        data=res[-1]
        for i in range(0,len(data)-1):
            temp.append(data[i]+data[i+1])
        temp.append(1)
        res.append(temp)
        result+=1

print(res)