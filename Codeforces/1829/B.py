t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    c=0
    for i in range(n):
        if a[i]==0:
            c+=1
            m=max(m,c)
        else:
            c=0
    print(m)