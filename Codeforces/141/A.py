s=input()
l=input()
p=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
for i in l:
    d[i]=d.get(i,0)+1
f={}
for i in p:
    f[i]=f.get(i,0)+1
if d==f:
    print("YES")
else:
    print("NO")
    