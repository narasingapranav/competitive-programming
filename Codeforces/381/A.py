n=int(input())
l=list(map(int,input().split()))
s=0
d=0
t=1
while len(l)>0:
    if len(l)==1 and t==1:
        s+=l[0]
        break
    if len(l)==1 and t==0:
        d+=l[0]
        break
    s+=max(l[0],l[-1])
    if l[0]>l[-1]:
        l.pop(0)
    else:
        l.pop()
    t=0
    d+=max(l[0],l[-1])
    if l[0]>l[-1]:
        l.pop(0)
    else:
        l.pop()
    t=1
print(s,d)

'''
s-7 5 3 1
d-6 4 2
'''