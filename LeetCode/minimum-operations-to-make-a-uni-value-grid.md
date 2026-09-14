# 🟠 minimum-operations-to-make-a-uni-value-grid — Minimum Operations to Make a Uni-Value Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) &nbsp;|&nbsp; **Solved:** 2026-04-28

---

## 📝 Summary

Accepted solution for Minimum Operations to Make a Uni-Value Grid on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minOperations(self, grid, x):
        arr = []
        for row in grid:
            for val in row:
                arr.append(val)
        arr.sort()
        median = arr[len(arr) // 2]
        operations = 0
        for num in arr:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            operations += diff // x
        return operations
```

</details>
