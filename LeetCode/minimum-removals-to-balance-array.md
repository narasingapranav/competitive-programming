# 🟠 minimum-removals-to-balance-array — Minimum Removals to Balance Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-removals-to-balance-array/) &nbsp;|&nbsp; **Solved:** 2026-02-06

---

## 📝 Summary

Accepted solution for Minimum Removals to Balance Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minRemoval(self,nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 0
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len
```

</details>
