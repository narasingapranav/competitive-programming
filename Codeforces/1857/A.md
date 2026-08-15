# 🔵 1857A — Array Coloring

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1857/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Determine whether an array can be split into two subsets such that the sums of the elements in both subsets have the same parity.

## 🔍 Key Observation

Two numbers have the same parity if and only if their sum is even, meaning the array can be split into two subsets with equal parity sums if and only if the sum of all elements in the array is even.

## ⚙️ Algorithm

**Parity analysis**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`math` `parity` `greedy`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if sum(a)%2==0:
        print("YES")
    else:
        print("NO")
```

</details>
