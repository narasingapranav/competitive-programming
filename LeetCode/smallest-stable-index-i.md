# 🟠 smallest-stable-index-i — Smallest Stable Index I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-stable-index-i/) &nbsp;|&nbsp; **Solved:** 2026-09-04

---

## 📝 Summary

Accepted solution for Smallest Stable Index I on LeetCode.

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
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            lh=nums[0:(i+1)]
            rh=nums[i:]
            if max(lh)-min(rh)<=k:
                return i
        return -1
```

</details>
