# 🟠 maximum-matrix-sum — Maximum Matrix Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-matrix-sum/) &nbsp;|&nbsp; **Solved:** 2026-01-05

---

## 📝 Summary

Accepted solution for Maximum Matrix Sum on LeetCode.

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
    def maxMatrixSum(self, matrix):
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    neg_count += 1
                total += abs(num)
                min_abs = min(min_abs, abs(num))
        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
```

</details>
