# 🟠 rotate-array — Rotate Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-array/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Accepted solution for Rotate Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=nums[(n-k):]+nums[:(n-k)]
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

</details>
