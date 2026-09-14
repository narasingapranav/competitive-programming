# 🟠 removing-minimum-and-maximum-from-array — Removing Minimum and Maximum From Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) &nbsp;|&nbsp; **Solved:** 2026-08-30

---

## 📝 Summary

Accepted solution for Removing Minimum and Maximum From Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minp, maxp, minel, maxel, L = 0, 0, float('inf'), float('-inf'), len(nums)
        for i, n in enumerate(nums):
            if n > maxel:
                maxel = n
                maxp = i
            if n < minel:
                minel = n
                minp = i
        
        left, right = min(minp, maxp), max(minp, maxp)

        return min(right + 1, L - left, left + 1 + (L - right))
```

</details>
