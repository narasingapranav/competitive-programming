# 🔵 1335A — Candies and Two Sisters

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1335/A) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Determine the number of ways to divide n candies between two sisters such that both receive at least one candy and the first sister receives strictly more candies than the second.

## 🔍 Key Observation

The second sister can receive anywhere from 1 to floor((n - 1) / 2) candies, making the total number of valid distributions equal to (n - 1) // 2.

## ⚙️ Algorithm

**Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    print((n-1)//2)
```

</details>
