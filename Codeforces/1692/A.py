t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    tim=l[0]
    c=0
    for i in range(1,len(l)):
        if l[i]>tim:
            c+=1
    print(c)