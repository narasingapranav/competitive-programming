# 🔵 1352A — Sum of Round Numbers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1352/A) &nbsp;|&nbsp; **Solved:** 2026-08-01

---

## 📝 Summary

Given a positive integer, break it down into a minimum number of round numbers, where a round number has at most one non-zero digit.

## 🔍 Key Observation

Each non-zero digit in the base-10 representation of the number directly corresponds to a distinct round number equal to the digit multiplied by its positional power of 10.

## ⚙️ Algorithm

**Base-10 digit extraction**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(log n)` |

## 🏷️ Tags

`implementation` `math` `digits`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
for _ in range(n):
    l=int(input())
    res=[]
    while l>0:
        res.append(l%10)
        l//=10
    for i in range(len(res)):
        res[i]=res[i]*10**i
    c=[i for i in res if i!=0][::-1]
    print(len(c))
    print(*c)
```

</details>
