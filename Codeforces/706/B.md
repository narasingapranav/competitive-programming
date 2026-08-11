# 🔵 706B — Interesting drink

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/706/B) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Given the prices of drinks in n shops and q daily budgets, determine how many shops sell a drink within each day's budget.

## 🔍 Key Observation

Sorting the drink prices enables the use of upper bound binary search to efficiently count the number of shops with prices less than or equal to a given budget.

## ⚙️ Algorithm

**Sorting + Binary search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O((n + q) log n)` | `O(n)` |

## 🏷️ Tags

`binary search` `sorting`

<details>
<summary>💻 View solution</summary>

```python
from bisect import bisect_right

n = int(input())
prices = list(map(int, input().split()))

prices.sort()

q = int(input())

for _ in range(q):
    m = int(input())
    print(bisect_right(prices, m))
```

</details>
