nums=[1, 2, 3, 6, 7, 5, 7]

s=sum(nums)

n=len(nums)
sn=int((n*(n+1))/2)

s2n=int((n*(n+1)*((2*n)+1))/6)

s2=0

s2=sum(i*i for i in nums)

val1=s-sn       #x-y =val1

val2=s2-s2n    #x^2 -y^2 = val2  => (x+y)(x-y)=val2

val2=val2/val1

x=int((val1+val2)/2)

y=x-val1

print(x,y)








