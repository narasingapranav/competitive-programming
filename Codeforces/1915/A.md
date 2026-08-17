# 🔵 1915A — Odd One Out

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1915/A) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Given three numbers where exactly two are equal, find the single unique number that differs from the rest.

## 🔍 Key Observation

XORing a number with itself results in 0 (x ^ x = 0), so taking the bitwise XOR of all three numbers cancels out the identical pair and leaves the unique number.

## ⚙️ Algorithm

**Bitwise XOR**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`bitmasks` `implementation`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    ans=0
    for i in l:
        ans^=i
    print(ans)
```

</details>
