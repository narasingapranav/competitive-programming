# 🔵 1814A — Coins

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1814/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Determine if a target sum n can be represented as a non-negative linear combination of coins with values 2 and k.

## 🔍 Key Observation

Any even target sum can be formed using only 2-coins, while an odd target sum requires k to be odd so that using one k-coin leaves an even remainder that can be fulfilled with 2-coins.

## ⚙️ Algorithm

**Parity analysis**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math` `implementation`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        print("YES")
    elif k%2==1:
        print("YES")
    else:
        print("NO")
```

</details>
