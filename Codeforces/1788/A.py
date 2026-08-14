t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=a.count(2)
    if c&1:
        print(-1)
    else:
        n=c//2
        b=0
        ans=0
        for i in range(len(a)):
            if a[i]==2:
                b+=1
            if b==n:
                ans=i+1
                break
        print(ans)