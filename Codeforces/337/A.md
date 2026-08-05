# 🔵 337A — Puzzles

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/337/A) &nbsp;|&nbsp; **Solved:** 2026-08-05

---

## 📝 Summary

Select $n$ puzzles out of $m$ available choices such that the difference between the largest and smallest puzzle size among the selected ones is minimized.

## 🔍 Key Observation

After sorting the puzzle sizes, the optimal subset of $n$ puzzles will always correspond to a contiguous subsegment of length $n$.

## ⚙️ Algorithm

**Sorting + Sliding Window**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m log m)` | `O(m)` |

## 🏷️ Tags

`sorting` `greedy` `sliding-window`

<details>
<summary>💻 View solution</summary>

```python
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
res=float('inf')
for i in range(m-n+1):
    if l[i+n-1]-l[i]<res:
        res=min(res,l[i+n-1]-l[i])
print(res)
```

</details>
