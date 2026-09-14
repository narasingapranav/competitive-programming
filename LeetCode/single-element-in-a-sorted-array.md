# 🟠 single-element-in-a-sorted-array — Single Element in a Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-08-26

---

## 📝 Summary

Accepted solution for Single Element in a Sorted Array on LeetCode.

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
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x^=i
        return x
```

</details>
