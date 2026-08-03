from collections import Counter
n=int(input())
s=[input() for _ in range(n)]
c=Counter(s)
initialcount={i: c[i] for i in c}
for i in s:
    if c[i]==initialcount[i]:
        print("OK")
        c[i]-=1
    else:
        print(i+str(initialcount[i]-c[i]))
        c[i]-=1