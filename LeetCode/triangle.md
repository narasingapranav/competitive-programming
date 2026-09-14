# 🟠 triangle — Triangle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/triangle/) &nbsp;|&nbsp; **Solved:** 2025-08-24

---

## 📝 Summary

Accepted solution for Triangle on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        min_path_sum = [0] * (num_rows + 1)
        for row in range(num_rows - 1, -1, -1):
            for col in range(row + 1):
               min_path_sum[col] = min(min_path_sum[col], min_path_sum[col + 1]) + triangle[row][col]
        return min_path_sum[0]
```

</details>
