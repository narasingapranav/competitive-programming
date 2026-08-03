n, k = map(int, input().split())
odd = (n + 1) // 2
if k <= odd:
    print(2 * k - 1)
else:
    print(2 * (k - odd))