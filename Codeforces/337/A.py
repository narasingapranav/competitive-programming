n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
res=float('inf')
for i in range(m-n+1):
    if l[i+n-1]-l[i]<res:
        res=min(res,l[i+n-1]-l[i])
print(res)