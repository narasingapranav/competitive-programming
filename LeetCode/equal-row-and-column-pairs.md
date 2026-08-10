# 🟠 equal-row-and-column-pairs — Equal Row and Column Pairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Given an n x n grid, count the number of pairs (r, c) such that row r and column c contain identical elements in the same order.

## 🔍 Key Observation

Converting rows to immutable tuples and storing their frequencies in a hash map allows checking each column tuple against all rows in fast O(n) time.

## ⚙️ Algorithm

**Hash Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`hash-table` `matrix` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        d={}
        for i in range(n):
            t=tuple(grid[i])
            d[t]=d.get(t,0)+1
        ans=0
        for j in range(n):
                col=tuple(grid[i][j] for i in range(n))
                if col in d:
                    ans+=d[col]
        return ans
```

</details>
