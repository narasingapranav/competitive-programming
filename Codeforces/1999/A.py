t=int(input())
for _ in range(t):
    i=int(input())
    res=0
    while i>0:
        res += i%10
        i//=10
    print(res)