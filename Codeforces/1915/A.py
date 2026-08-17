t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    ans=0
    for i in l:
        ans^=i
    print(ans)