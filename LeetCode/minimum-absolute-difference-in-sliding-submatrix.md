# 🟠 minimum-absolute-difference-in-sliding-submatrix — Minimum Absolute Difference in Sliding Submatrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/) &nbsp;|&nbsp; **Solved:** 2026-03-20

---

## 📝 Summary

Accepted solution for Minimum Absolute Difference in Sliding Submatrix on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                v = sorted(set(
                    grid[x][y]
                    for x in range(i, i + k)
                    for y in range(j, j + k)
                ))
                if len(v) <= 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = min(v[p+1] - v[p] for p in range(len(v) - 1))

        return ans
```

</details>
