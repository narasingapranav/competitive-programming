n=int(input())
l=list(map(int,input().split()))
c=0
h=0
for i in range(n):
    if l[i]<0 and h==0:
        c+=1
    if h>0 and l[i]<0:
        h-=1
    if l[i]>0:
        h+=l[i]
print(c)