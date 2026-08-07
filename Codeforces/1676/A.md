# 🔵 1676A — Lucky?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1676/A) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Determine whether the sum of the first three digits of a six-digit string is equal to the sum of the last three digits.

## 🔍 Key Observation

Splitting the six-digit string into two equal halves allows direct comparison of their respective digit sums.

## ⚙️ Algorithm

**String manipulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=input()
    mid=len(n)//2
    n1=(n[:mid])
    n2=(n[mid:])
    s1=sum([int(i) for i in n1])
    s2=sum([int(i) for i in n2])
    if s1==s2:
        print("YES")
    else:
        print("NO")
```

</details>
