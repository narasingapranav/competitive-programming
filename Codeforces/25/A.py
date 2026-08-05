n=int(input())
l=list(map(int,input().split()))
rem=[i&1 for i in l[:3]]
m=0 if rem.count(1)>=2 else 1
for i in range(len(l)):
    if l[i]&1==m:
        print(i+1)
        break