# 🔵 1853A — Desorting

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1853/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Determine the minimum number of operations required to make an array unsorted, where each operation increments a prefix of elements and decrements the remaining suffix.

## 🔍 Key Observation

If the array is already unsorted, 0 operations are required; otherwise, the easiest pair of adjacent elements to desort is the pair with the smallest difference d, which takes d // 2 + 1 operations.

## ⚙️ Algorithm

**Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`greedy` `math` `brute force`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if any (a[i] > a[i + 1] for i in range(n - 1)):
        print(0)
        continue
    d=min(a[i + 1] - a[i] for i in range(n - 1))
    print(d//2 + 1)
```

</details>
