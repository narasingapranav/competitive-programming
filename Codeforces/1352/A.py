n=int(input())
for _ in range(n):
    l=int(input())
    res=[]
    while l>0:
        res.append(l%10)
        l//=10
    for i in range(len(res)):
        res[i]=res[i]*10**i
    c=[i for i in res if i!=0][::-1]
    print(len(c))
    print(*c)