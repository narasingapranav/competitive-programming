# 🔵 1873A — Short Sort

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Determine if a string of length three containing 'a', 'b', and 'c' can be transformed into 'abc' using at most one character swap.

## 🔍 Key Observation

Out of the 6 possible permutations of 'abc', only 'bca' and 'cab' require more than one swap to be sorted, as every other permutation has at least one character already in its correct position.

## ⚙️ Algorithm

**Implementation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `strings` `brute force`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    s=input()
    if s=="cba" or s=="acb" or s=="bac" or s=="abc":
        print("YES")
    else:
        print("NO")
```

</details>
