t=int(input())
MOD=10**9+7
for _ in range(t):
    n,k=map(int,input().split())
    ans=0
    pow=1
    while k>0:
        if k&1:
            ans=(ans+pow)%MOD
        pow=(pow*n)%MOD
        k>>=1
    print(ans)