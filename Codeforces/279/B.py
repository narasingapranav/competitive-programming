n, t = map(int, input().split())
a = list(map(int, input().split()))
left = 0
total = 0
ans = 0
for right in range(n):
    total += a[right]
    while total > t:
        total -= a[left]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)