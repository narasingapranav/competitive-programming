# 🔵 1999A — A+B Again?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1999/A) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Given a two-digit positive integer, calculate and output the sum of its digits.

## 🔍 Key Observation

The digits of a base-10 number can be iteratively extracted by taking the remainder when divided by 10 and then integer-dividing by 10.

## ⚙️ Algorithm

**Digit extraction / Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    i=int(input())
    res=0
    while i>0:
        res += i%10
        i//=10
    print(res)
```

</details>
