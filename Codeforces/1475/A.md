# 🔵 1475A — Odd Divisor

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1475/A) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Determine if a given integer n has an odd divisor greater than 1.

## 🔍 Key Observation

A number has an odd divisor greater than 1 if and only if it is not a power of two.

## ⚙️ Algorithm

**Repeated division by 2**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) per testcase` | `O(1)` |

## 🏷️ Tags

`math` `number theory` `bit manipulation`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    while n%2==0:
        n//=2
    if n==1:
        print("NO")
    else:
        print("YES")
```

</details>
