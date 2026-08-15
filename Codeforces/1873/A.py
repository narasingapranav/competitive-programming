t=int(input())
for _ in range(t):
    s=input()
    if s=="cba" or s=="acb" or s=="bac" or s=="abc":
        print("YES")
    else:
        print("NO")