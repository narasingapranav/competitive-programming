# 🔵 151A — Soft Drinking

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/151/A) &nbsp;|&nbsp; **Solved:** 2026-08-05

---

## 📝 Summary

Determine how many toasts each of the n friends can make given limited quantities of drink, lime slices, and salt, where each toast requires specific amounts of each ingredient.

## 🔍 Key Observation

The total number of toasts that can be made is limited by whichever ingredient runs out first (the bottleneck), so taking the minimum of the drinks, lime slices, and salt capacity yields the total possible toasts.

## ⚙️ Algorithm

**Direct calculation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
n, k, l, c, d, p, nl, np=map(int, input().split())
drinks=k*l
s=drinks//nl
toasts=c*d
salt=p//np
print(min(s, toasts, salt)//n)
```

</details>
