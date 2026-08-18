t=int(input())
for _ in range(t):
    n=int(input())
    b=input()
    l=0
    r=n-1
    while l<r and b[l]!=b[r]:
        l+=1
        r-=1
    print(r-l+1 if l<=r else 0)