n,k=map(int,input().split())
remtime=240-k
c=0
for i  in range(1,n+1):
    remtime-=5*i
    if remtime<0:
        break
    c+=1
print(c)