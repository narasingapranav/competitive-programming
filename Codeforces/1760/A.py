t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    mx,mi=max(l),min(l)
    for i in l:
        if i!=mx and i!=mi:
            print(i)
            break