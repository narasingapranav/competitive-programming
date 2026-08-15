t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if any (a[i] > a[i + 1] for i in range(n - 1)):
        print(0)
        continue
    d=min(a[i + 1] - a[i] for i in range(n - 1))
    print(d//2 + 1)