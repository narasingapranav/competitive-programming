n=int(input())
MOD=10**9+7
res=1
for _ in range(n-1):
    res=(res*4)%MOD
    res=(res*res)%MOD
print((6*res)%MOD)