# 🟠 minimum-difference-between-highest-and-lowest-of-k-scores — Minimum Difference Between Highest and Lowest of K Scores

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Accepted solution for Minimum Difference Between Highest and Lowest of K Scores on LeetCode.

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
from itertools import combinations
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        a=float('inf')
        for i in range(len(nums)-k+1):
            a=min(a,nums[i+k-1]-nums[i])
        return a
```

</details>
