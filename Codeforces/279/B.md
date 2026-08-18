# 🔵 279B — Books

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/279/B) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Find the maximum number of consecutive books that can be read within a given total time limit t.

## 🔍 Key Observation

Since all book reading times are non-negative, the total time for any contiguous range of books increases monotonically as the range expands, allowing the optimal subarray to be found efficiently using a sliding window.

## ⚙️ Algorithm

**Two pointers / Sliding window**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`two pointers` `sliding window` `greedy` `arrays`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
