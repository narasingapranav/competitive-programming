n=int(input())
l=list(map(int,input().split()))
c=1
maxc=1
for i in range(0,n-1):
    if l[i]>l[i+1]:
        c=1
    else:
        c+=1
    maxc=max(maxc,c)
print(maxc)