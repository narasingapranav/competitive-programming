t=int(input())
for _ in range(t):
    n=input()
    mid=len(n)//2
    n1=(n[:mid])
    n2=(n[mid:])
    s1=sum([int(i) for i in n1])
    s2=sum([int(i) for i in n2])
    if s1==s2:
        print("YES")
    else:
        print("NO")