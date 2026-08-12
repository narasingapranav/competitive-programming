# 🔵 1807A — Plus or Minus

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1807/A) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given three integers a, b, and c, determine whether a + b = c or a - b = c and output '+' or '-' respectively.

## 🔍 Key Observation

Since it is guaranteed that either a + b = c or a - b = c holds, checking if a + b == c is sufficient to distinguish between the two cases.

## ⚙️ Algorithm

**Implementation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) per test case` | `O(1)` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a+b==c:
        print('+')
    else:
        print('-')
```

</details>
