# 🟠 rotate-function — Rotate Function

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-function/) &nbsp;|&nbsp; **Solved:** 2026-05-01

---

## 📝 Summary

Accepted solution for Rotate Function on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

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
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_val = f
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            max_val = max(max_val, f)
        return max_val
```

</details>
