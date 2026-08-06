import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
c=0
mi=l[0]
mx=l[0]
for i in range(1,n):
    if l[i]<mi:
        mi=l[i]
        c+=1
    elif l[i]>mx:
        mx=l[i]
        c+=1
print(c)