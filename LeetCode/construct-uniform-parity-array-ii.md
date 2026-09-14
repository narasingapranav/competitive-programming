# 🟠 construct-uniform-parity-array-ii — Construct Uniform Parity Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-03

---

## 📝 Summary

Accepted solution for Construct Uniform Parity Array II on LeetCode.

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
    def uniformArray(self, nums1: list[int]) -> bool:
        a=nums1[0]
        flag=False
        for i in nums1:
            if i<a:
                a=i
            if i&1:
                flag=True
        if a&1:
            return True
        return not flag
```

</details>
