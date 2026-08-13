t=int(input())
for _ in range(t):
    n,c=input().split()
    n=int(n)
    s=input()
    allcount=[]
    for x in range(1,n+1):
        count=0
        for i in range(x,n+1,x):
            if s[i-1]!=c:
                count+=1
        allcount.append(count)
    if all(s[i] == c for i in range(n)):
        print(0)

    elif 0 in allcount:
        x = allcount.index(0) + 1
        print(1)
        print(x)

    else:
        print(2)
        print(n - 1, n)