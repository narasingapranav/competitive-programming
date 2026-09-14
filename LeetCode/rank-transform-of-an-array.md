# 🟠 rank-transform-of-an-array — Rank Transform of an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Accepted solution for Rank Transform of an Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = []
        num_rank = {}

        for num in arr:
            if num not in num_rank:
                unique_arr.append(num)
                num_rank[num] = 0

        unique_arr.sort()

        for i, num in enumerate(unique_arr):
            num_rank[num] = i + 1

        return [num_rank[num] for num in arr]
```

</details>
