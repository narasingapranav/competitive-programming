s,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:x[0])
for i in l:
    s-=i[0]
    if s<=0:
        print("NO")
        break
    s+=i[0]+i[1]
else:
    print("YES")