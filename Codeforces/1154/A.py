l=list(map(int,input().split()))
t=max(l)
l.pop(l.index(t))
x,y,z=l
a=(x+y-z)//2
b=(x+z-y)//2
c=(y+z-x)//2
print(a,b,c)