# 🔵 581A — Vasya the Hipster

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/581/A) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given the number of red and blue socks, calculate the maximum number of days Vasya can wear two different-colored socks, followed by how many days he can wear same-colored socks.

## 🔍 Key Observation

The number of different-colored pairs is bounded by min(a, b), and the remaining socks of the larger group can be paired together by dividing their difference by 2.

## ⚙️ Algorithm

**Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
a,b=map(int,input().split())
c=min(a,b)
k=abs(a-b)//2
print(c,k)
```

</details>
